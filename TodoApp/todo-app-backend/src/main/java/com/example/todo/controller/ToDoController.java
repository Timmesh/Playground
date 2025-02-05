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
    public ToDo updateToDo(@PathVariable("id") Long id, @RequestBody ToDo todo) {
        return service.updateToDo(id, todo);
    }

    @DeleteMapping("/{id}")
    public void deleteToDo(@PathVariable("id") Long id) {
        service.deleteToDoById(id);
    }
}
