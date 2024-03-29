package com.timmesh.rest.webservices.restfulwebservices.resource;

import java.net.URI;
import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.hateoas.EntityModel;
import org.springframework.hateoas.server.mvc.WebMvcLinkBuilder;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import com.timmesh.rest.webservices.restfulwebservices.entity.Post;
import com.timmesh.rest.webservices.restfulwebservices.entity.User;
import com.timmesh.rest.webservices.restfulwebservices.service.PostService;
import com.timmesh.rest.webservices.restfulwebservices.service.UserService;

@RestController
public class UserResource {

	@Autowired
	private UserService service;

	@Autowired
	private PostService postService;

	@GetMapping("/users")
	public List<User> retrieveAllUsers() {
		return service.findAll();
	}

	@GetMapping("/users/{id}")
	public EntityModel<User> retrieveUser(@PathVariable int id) {
		User user = service.findOne(id);
		// "all-users", SERVER_PATH + "/users"
		// retrieveAllUsers
		EntityModel<User> entityModel = EntityModel.of(user);
		WebMvcLinkBuilder linkTo = WebMvcLinkBuilder
				.linkTo(WebMvcLinkBuilder.methodOn(this.getClass()).retrieveAllUsers());
		entityModel.add(linkTo.withRel("all-users"));
		return entityModel;
	}

	//
	// input - details of user
	// output - CREATED & Return the created URI
	@PostMapping("/users")
	public ResponseEntity<Object> createUser(@Valid @RequestBody User user) {
		User savedUser = service.save(user);
		// CREATED
		// /user/{id} savedUser.getId()
		URI location = ServletUriComponentsBuilder.fromCurrentRequest().path("/{id}").buildAndExpand(savedUser.getId())
				.toUri();
		return ResponseEntity.created(location).build();
	}

	@DeleteMapping("/users/{id}")
	public void deleteUser(@PathVariable int id) {
		service.deleteById(id);
	}

	@GetMapping("/users/{id}/posts")
	public List<com.timmesh.rest.webservices.restfulwebservices.entity.Post> retrieveAllUsers(@PathVariable int id) {
		return service.retreiveAllUserPosts(id);
	}

	@PostMapping("/users/{id}/posts")
	public ResponseEntity<Object> createPost(@PathVariable int id, @RequestBody Post post) {
		User user = service.findOne(id);
		post.setUser(user);
		postService.save(post);
		URI location = ServletUriComponentsBuilder.fromCurrentRequest().path("/{id}").buildAndExpand(post.getId())
				.toUri();
		return ResponseEntity.created(location).build();

	}
}
