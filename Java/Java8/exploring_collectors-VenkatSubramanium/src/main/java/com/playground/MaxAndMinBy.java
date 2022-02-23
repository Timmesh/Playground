package com.playground;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

import com.playground.entity.Person;

/**
 * @author USER Grouping the people based on their names.
 */
public class MaxAndMinBy {
	public static List<Person> createPeople() {
		return Arrays.asList(new Person("Sara", 20), new Person("Sara", 22), new Person("Bob", 20),
				new Person("Paula", 32), new Person("Paul", 32), new Person("Jack", 2), new Person("Jack", 72),
				new Person("Jill", 11));
	}

	public static List<Person> createPeopleWithGender() {
		return Arrays.asList(new Person("Sara", 20, "F"), new Person("Sara", 22, "F"), new Person("Bob", 20, "M"),
				new Person("Paula", 32, "F"), new Person("Paul", 32, "M"), new Person("Jack", 2, "M"),
				new Person("Jack", 72, "M"), new Person("Jill", 11, "M"));
	}

	public static void main(String[] args) {
		System.out.println(createPeople().stream().collect(Collectors.maxBy(Comparator.comparing(Person::getAge))));

		System.out.println(createPeople().stream().collect(Collectors.minBy(Comparator.comparing(Person::getAge))));

		System.out.println(createPeople().stream().collect(Collectors
				.collectingAndThen(Collectors.maxBy(Comparator.comparing(Person::getAge))
						, p -> p.map(Person::getName).orElse(""))));
	}
}