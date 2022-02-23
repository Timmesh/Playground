package com.timmesh.microservices.limitsservice.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.timmesh.microservices.limitsservice.bean.Limits;
import com.timmesh.microservices.limitsservice.configuration.Configuration;

@RestController
public class LimitsController {

	@Autowired
	private Configuration configuration;

	@GetMapping("/limits")
	private Limits retreiveLimits() {
		return new Limits(configuration.getMinimum(), configuration.getMaximum());
	}

}
