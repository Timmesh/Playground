const API_URL = "http://localhost:8081/api/todos";

// Fetch and display todos
async function fetchTodos() {
    const response = await fetch(API_URL);
    const todos = await response.json();
    const todoList = document.getElementById("todoList");
    todoList.innerHTML = "";
    todos.forEach(todo => {
        let li = document.createElement("li");
        li.innerHTML = `${todo.task} 
            <button onclick="updateTodo(${todo.id}, '${todo.task}')">Edit</button>
            <button onclick="deleteTodo(${todo.id})">Delete</button>`;
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

    await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task: newTask, completed: false })
    });

    fetchTodos();
}

// Delete a ToDo
async function deleteTodo(id) {
    if (confirm("Are you sure you want to delete this task?")) {
        await fetch(`${API_URL}/${id}`, { method: "DELETE" });
        fetchTodos();
    }
}

// Load todos on page load
window.onload = fetchTodos;
