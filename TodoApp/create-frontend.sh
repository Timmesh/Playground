#!/bin/bash

# Set project directory
PROJECT_DIR="todo-app-frontend"

# Create frontend project folder
mkdir -p $PROJECT_DIR/{css,js}

# Create index.html
cat <<EOL > $PROJECT_DIR/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ToDo App</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <h1>ToDo App</h1>
    
    <input type="text" id="taskInput" placeholder="Enter new task">
    <button onclick="addTodo()">Add Task</button>

    <ul id="todoList"></ul>

    <script src="js/app.js"></script>
</body>
</html>
EOL

# Create JavaScript (app.js)
cat <<EOL > $PROJECT_DIR/js/app.js
const API_URL = "http://localhost:8080/api/todos";

// Fetch and display todos
async function fetchTodos() {
    const response = await fetch(API_URL);
    const todos = await response.json();
    const todoList = document.getElementById("todoList");
    todoList.innerHTML = "";
    todos.forEach(todo => {
        let li = document.createElement("li");
        li.innerHTML = \`\${todo.task} 
            <button onclick="updateTodo(\${todo.id}, '\${todo.task}')">Edit</button>
            <button onclick="deleteTodo(\${todo.id})">Delete</button>\`;
        todoList.appendChild(li);
    });
}

// Add a new ToDo
async function addTodo() {
    const task = document.getElementById("taskInput").value;
    if (task.trim() === "") return alert("Task cannot be empty");

    await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task, completed: false })
    });

    document.getElementById("taskInput").value = "";
    fetchTodos();
}

// Update a ToDo
async function updateTodo(id, oldTask) {
    const newTask = prompt("Update task:", oldTask);
    if (newTask === null || newTask.trim() === "") return;

    await fetch(\`\${API_URL}/\${id}\`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task: newTask, completed: false })
    });

    fetchTodos();
}

// Delete a ToDo
async function deleteTodo(id) {
    if (confirm("Are you sure you want to delete this task?")) {
        await fetch(\`\${API_URL}/\${id}\`, { method: "DELETE" });
        fetchTodos();
    }
}

// Load todos on page load
window.onload = fetchTodos;
EOL

# Create CSS (style.css)
cat <<EOL > $PROJECT_DIR/css/style.css
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    text-align: center;
}
input, button {
    margin: 5px;
    padding: 10px;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    margin: 5px 0;
    padding: 10px;
    background: #f4f4f4;
    display: flex;
    justify-content: space-between;
}
EOL

echo "Frontend setup complete! Open 'todo-app-frontend/index.html' in a browser."

