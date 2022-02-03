package com.timmesh.rest.webservices.restfulwebservices.service;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.timmesh.rest.webservices.restfulwebservices.entity.User;
import com.timmesh.rest.webservices.restfulwebservices.exception.UserNotFoundException;
import com.timmesh.rest.webservices.restfulwebservices.repository.UserJPARepository;

@Component
public class UserService {

	@Autowired
	UserJPARepository userRepository;

	public List<User> findAll() {
		return userRepository.findAll();
	}

	public User save(User user) {
		return userRepository.save(user);

	}

	public User findOne(int id) {
		Optional<User> user = userRepository.findById(id);
		if (!user.isPresent()) {
			throw new UserNotFoundException("id-" + id);
		}
		return user.get();
	}

	public void deleteById(int id) {
		userRepository.deleteById(id);
	}

}
