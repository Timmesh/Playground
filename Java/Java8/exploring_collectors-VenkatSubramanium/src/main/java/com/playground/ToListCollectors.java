package com.playground;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import com.playground.entity.Person;

/**
 * @author USER
 * Immutable List.
 */
public class ToListCollectors {
	public static List<Person> createPeople() {
		return Arrays.asList(new Person("Sara", 20), new Person("Sara2", 22), new Person("Bob", 20),
				new Person("Paula", 32), new Person("Paul", 32), new Person("Jack", 2), new Person("Jack2", 72),
				new Person("Jill", 12));
	}

	public static void main(String[] args) {
		List<Integer> ages = createPeople().stream().map(p->p.getAge())
				.collect(Collectors.toList());
		System.out.println(ages);
		
		// ImmutableList - Java 10
		List<Integer> ages2 = createPeople().stream().map(p->p.getAge())
				.collect(Collectors.toUnmodifiableList());
		System.out.println(ages2);
		
	}
}