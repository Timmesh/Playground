package com.timmesh.rest.webservices.restfulwebservices.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.timmesh.rest.webservices.restfulwebservices.entity.User;

@Repository
public interface UserJPARepository extends JpaRepository<User, Integer> {
}
