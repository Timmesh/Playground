package com.timmesh.springsecurity_ldap;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserResource {

	@GetMapping("/")
	public String retrieve() {
		return "Timmesh";
	}
	
	@GetMapping("/admin")
	public String retrieveAdmin() {
		return "Nakul";
	}
	
	@GetMapping("/user")
	public String retrieveUser() {
		return "Pals";
	}

}
