package com.playground;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import com.playground.entity.Person;

/**
 * @author USER Example of impure Function- DONT DO THIS
 */
public class Sample2 {
	public static List<Person> createPeople() {
		return Arrays.asList(new Person("Sara", 20), new Person("Sara", 22), new Person("Bob", 20),
				new Person("Paula", 32), new Person("Paul", 32), new Person("Jack", 2), new Person("Jack", 72),
				new Person("Jill", 12));
	}

	public static void main(String[] args) {
		List<Person> people = createPeople();
		List<String> listOfPersonAbove30 = new ArrayList<String>();
		people.stream()
			.filter(p -> p.getAge() > 30) // Pure Function
			.map(p -> p.getName()) // Pure Function
			.forEach(v -> listOfPersonAbove30.add(v)); // ImPure Function
		System.out.println(listOfPersonAbove30);
	}
}