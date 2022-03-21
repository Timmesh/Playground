package com.timmesh.SpringSecurity;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserResource {

	@GetMapping("/user")
	public String retrieveUser() {
		return "Timmesh";
	}

}
