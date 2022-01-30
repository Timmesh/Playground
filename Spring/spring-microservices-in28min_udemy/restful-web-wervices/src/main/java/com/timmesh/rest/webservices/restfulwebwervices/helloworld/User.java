package com.timmesh.rest.webservices.restfulwebwervices.helloworld;

import java.util.Date;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@AllArgsConstructor
@ToString
public class User {

	private Integer id;

	private String name;

	private Date birthDate;

}
