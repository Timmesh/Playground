package com.playground;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

import com.playground.entity.Person;

/**
 * @author USER
 * Grouping the people based on their names.
 */
public class Sorting {

	public static List<Person> createPeople() {
		return Arrays.asList(new Person("Sara", 20), new Person("Sara", 22), new Person("Bob", 20),
				new Person("Paula", 32), new Person("Paul", 32), new Person("Jack", 2), new Person("Jack", 72),
				new Person("Jill", 11));
	}

	public static void main(String[] args) {
		createPeople().stream().sorted(Comparator.comparing(Person::getAge)).forEach(System.out::println);
		createPeople().stream().sorted(Comparator.comparing(Person::getAge).thenComparing(p -> p.getName()))
				.forEach(System.out::println);

	}
}