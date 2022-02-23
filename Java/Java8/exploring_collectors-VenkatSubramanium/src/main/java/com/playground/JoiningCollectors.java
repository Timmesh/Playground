package com.playground;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import com.playground.entity.Person;

/**
 * @author USER Create comma seperated names in uppercase of people older than
 *         30
 */
public class JoiningCollectors {
	public static List<Person> createPeople() {
		return Arrays.asList(new Person("Sara", 20), new Person("Sara2", 22), new Person("Bob", 20),
				new Person("Paula", 32), new Person("Paul", 32), new Person("Jack", 2), new Person("Jack2", 72),
				new Person("Jill", 12));
	}

	public static void main(String[] args) {
		String collect = createPeople().stream().filter(p -> p.getAge() > 30).map(p -> p.getName().toUpperCase())
				.collect(Collectors.joining(","));
		System.out.println(collect);
	}
}