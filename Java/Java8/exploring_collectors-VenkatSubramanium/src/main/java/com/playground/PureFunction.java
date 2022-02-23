package com.playground;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import com.playground.entity.Person;

/**
 * @author USER Example of pure Function
 */
public class PureFunction {
	public static List<Person> createPeople() {
		return Arrays.asList(new Person("Sara", 20), new Person("Sara", 22), new Person("Bob", 20),
				new Person("Paula", 32), new Person("Paul", 32), new Person("Jack", 2), new Person("Jack", 72),
				new Person("Jill", 12));
	}

	public static void main(String[] args) {
		List<Person> people = createPeople();
		List<String> listOfPersonAbove30 = people.stream()
				.filter(p -> p.getAge() > 30) // Pure Function
				.map(p -> p.getName()) // Pure Function
				.reduce(new ArrayList<String>(), (names, name) -> {
					names.add(name);
					return names;
				}, (names1, names2) -> {
					names1.addAll(names2);
					return names1;
				});
		System.out.println(listOfPersonAbove30);
		List<String> listOfPersonAbove30_2 = people.stream()
				.filter(p -> p.getAge() > 30) // Pure Function
				.map(p -> p.getName()) // Pure Function
				.collect(Collectors.toList());
		System.out.println(listOfPersonAbove30_2);
	}
}