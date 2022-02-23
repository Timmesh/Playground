package com.playground.entity;

public class Person {
	private final String name;
	private final int age;
	private String gender;

	public Person(String theName, int theAge) {
		name = theName;
		age = theAge;
	}
	
	public Person(String theName, int theAge, String gender) {
		name = theName;
		age = theAge;
		this.gender = gender;
	}

	public String getName() {
		return name;
	}

	public int getAge() {
		return age;
	}

	public String toString() {
		if(gender == null) {
			return String.format("%s -- %d", name, age);
		}
		return String.format("%s -- %d -- %s", name, age, gender);
	}

	public String getGender() {
		return gender;
	}
}
