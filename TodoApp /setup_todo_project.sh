#!/bin/bash

# Define project name
PROJECT_NAME="todo-app-backend"

# Define directory structure
mkdir -p $PROJECT_NAME/src/main/java/com/example/todo/controller
mkdir -p $PROJECT_NAME/src/main/java/com/example/todo/service
mkdir -p $PROJECT_NAME/src/main/java/com/example/todo/repository
mkdir -p $PROJECT_NAME/src/main/java/com/example/todo/entity
mkdir -p $PROJECT_NAME/src/main/resources

# Create pom.xml
cat > $PROJECT_NAME/pom.xml <<EOL
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>todo-app</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
EOL

# Create Java files with basic content
cat > $PROJECT_NAME/src/main/java/com/example/todo/controller/ToDoController.java <<EOL
package com.example.todo.controller;

import com.example.todo.entity.ToDo;
import com.example.todo.service.ToDoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/todos")
@CrossOrigin(origins = "*")
public class ToDoController {
    
    @Autowired
    private ToDoService service;

    @GetMapping
    public List<ToDo> getAllToDos() {
        return service.getAllToDos();
    }

    @PostMapping
    public ToDo createToDo(@RequestBody ToDo todo) {
        return service.addToDo(todo);
    }

    @PutMapping("/{id}")
    public ToDo updateToDo(@PathVariable Long id, @RequestBody ToDo todo) {
        return service.updateToDo(id, todo);
    }

    @DeleteMapping("/{id}")
    public void deleteToDo(@PathVariable Long id) {
        service.deleteToDoById(id);
    }
}
EOL

cat > $PROJECT_NAME/src/main/java/com/example/todo/service/ToDoService.java <<EOL
package com.example.todo.service;

import com.example.todo.entity.ToDo;
import com.example.todo.repository.ToDoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ToDoService {
    @Autowired
    private ToDoRepository repository;

    public List<ToDo> getAllToDos() {
        return repository.findAll();
    }

    public ToDo addToDo(ToDo todo) {
        return repository.save(todo);
    }

    public ToDo updateToDo(Long id, ToDo updatedToDo) {
        return repository.findById(id)
                .map(todo -> {
                    todo.setTask(updatedToDo.getTask());
                    todo.setCompleted(updatedToDo.isCompleted());
                    return repository.save(todo);
                })
                .orElseThrow(() -> new RuntimeException("ToDo not found"));
    }

    public void deleteToDoById(Long id) {
        repository.deleteById(id);
    }
}
EOL

cat > $PROJECT_NAME/src/main/java/com/example/todo/repository/ToDoRepository.java <<EOL
package com.example.todo.repository;

import com.example.todo.entity.ToDo;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ToDoRepository extends JpaRepository<ToDo, Long> {
}
EOL

cat > $PROJECT_NAME/src/main/java/com/example/todo/entity/ToDo.java <<EOL
package com.example.todo.entity;

import jakarta.persistence.*;

@Entity
@Table(name = "todos")
public class ToDo {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String task;
    private boolean completed;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getTask() { return task; }
    public void setTask(String task) { this.task = task; }
    public boolean isCompleted() { return completed; }
    public void setCompleted(boolean completed) { this.completed = completed; }
}
EOL

cat > $PROJECT_NAME/src/main/resources/application.properties <<EOL
spring.datasource.url=jdbc:mysql://localhost:3306/todo_db
spring.datasource.username=root
spring.datasource.password=root
spring.jpa.hibernate.ddl-auto=update
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.jpa.database-platform=org.hibernate.dialect.MySQL8Dialect
server.port=8080
EOL

echo "Project structure for $PROJECT_NAME created successfully."
