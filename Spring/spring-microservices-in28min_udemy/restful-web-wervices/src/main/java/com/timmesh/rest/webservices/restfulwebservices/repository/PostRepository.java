package com.timmesh.rest.webservices.restfulwebservices.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.timmesh.rest.webservices.restfulwebservices.entity.Post;

@Repository
public interface PostRepository extends JpaRepository<Post, Integer>{

}
