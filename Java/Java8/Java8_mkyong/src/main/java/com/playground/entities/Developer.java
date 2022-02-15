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

	public Developer(String name) {
		this.name = name;
	}
	
	
}