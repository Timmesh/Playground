package com.playground;

import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.function.Predicate;
import java.util.stream.Collectors;

import com.playground.entity.Person;

/**
 * @author USER Grouping the people based on their names.
 */
public class Filtering {
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

		// Filtering by age- Introduced in JAVA 9
		Map<String, List<Person>> output = createPeopleWithGender().stream().collect(Collectors
				.groupingBy(Person::getName, Collectors.filtering(e -> e.getAge() > 30, Collectors.toList())));
		output.values().stream().filter(Predicate.not(Collection::isEmpty)).forEach(System.out::print);
		System.out.println();
		output.entrySet().stream().filter(e -> !e.getValue().isEmpty()).forEach(System.out::print);
		output.entrySet().stream().filter(e -> !e.getValue().isEmpty()).forEach(e -> System.out.println(e.getKey()));

		System.out.println();
		System.out.println(output);

	}
}