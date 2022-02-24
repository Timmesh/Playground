package com.playground;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

import com.playground.entity.Person;

/**
 * @author USER
 * Map: name as Key and age as value
 */
public class ToMapCollector {
	public static List<Person> createPeople() {
		return Arrays.asList(new Person("Sara", 20), new Person("Sara2", 22), new Person("Bob", 20),
				new Person("Paula", 32), new Person("Paul", 32), new Person("Jack", 2), new Person("Jack2", 72),
				new Person("Jill", 12));
	}

	public static void main(String[] args) {
		// Imperative Style
		Map<String, Integer> nameAndAge = new HashMap<String, Integer>();
		for (Person person : createPeople()) {
			nameAndAge.put(person.getName(), person.getAge());
		}
		System.out.println(nameAndAge);
		
		// Functional Style
		Map<String, Integer> nameAndAge2 = createPeople().stream()
				.collect(Collectors.toMap(p -> p.getName(), p -> p.getAge()));
		System.out.println(nameAndAge2);

		Map<String, Person> nameAndPerson = createPeople().stream()
				.collect(Collectors.toMap(p -> p.getName(), Function.identity()));
		System.out.println("nameAndPerson"+nameAndPerson);

		
		Map<String, Integer> nameAndAge3 = createPeople().stream()
				.collect(Collectors.toMap(Person::getName, Person::getAge));
		System.out.println(nameAndAge3);
		
		Map<String, Long> nameAndAge4 = createPeople().stream()
				.collect(Collectors.groupingBy(Person::getName, Collectors.counting()));
		System.out.println(nameAndAge4);
	}
}