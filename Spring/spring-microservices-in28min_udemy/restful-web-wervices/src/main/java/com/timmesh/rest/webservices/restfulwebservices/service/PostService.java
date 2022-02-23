package com.timmesh.rest.webservices.restfulwebservices.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.timmesh.rest.webservices.restfulwebservices.entity.Post;
import com.timmesh.rest.webservices.restfulwebservices.repository.PostRepository;

@Component
public class PostService {

	@Autowired
	PostRepository postRepository;

	public Post save(Post post) {
		return postRepository.save(post);
	}
	
}
