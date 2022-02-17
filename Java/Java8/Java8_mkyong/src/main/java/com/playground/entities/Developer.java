package com.playground.entities;

import java.math.BigDecimal;
import java.time.LocalDate;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Setter
@Getter
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class Developer {

	String name;
	BigDecimal salary;
	LocalDate start;
	int age;

	public Developer(String name) {
		this.name = name;
	}

	public Developer(String name, BigDecimal salary) {
		super();
		this.name = name;
		this.salary = salary;
	}

	public Developer(String name, BigDecimal salary, LocalDate start) {
		super();
		this.name = name;
		this.salary = salary;
		this.start = start;
	}

	public Developer(String name, BigDecimal salary, int age) {
		super();
		this.name = name;
		this.salary = salary;
		this.age = age;
	}

}