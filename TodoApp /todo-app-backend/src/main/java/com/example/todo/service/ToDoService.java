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
