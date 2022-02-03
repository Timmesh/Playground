package com.timmesh.microservices.limitsservice.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.timmesh.microservices.limitsservice.bean.Limits;

@RestController
public class LimitsController {

	@GetMapping("/limits")
	private Limits retreiveLimits() {
		return new Limits(1, 100);
	}
	
}
