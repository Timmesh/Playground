package com.timmesh.rest.webservices.restfulwebservices.entity;

import java.util.Date;

import javax.validation.constraints.Past;
import javax.validation.constraints.Size;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@AllArgsConstructor
@ToString
@NoArgsConstructor
public class User {

	private Integer id;

	@Size(min=2, message="Name should have atleast 2 characters")
	private String name;

	@Past
	private Date birthDate;

}
