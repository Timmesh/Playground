package com.playground;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import com.playground.entity.Person;

/**
 * @author USER Partitioning the list into two
 */
public class PartitioningBy {
	public static List<Person> createPeople() {
		return Arrays.asList(new Person("Sara", 20), new Person("Sara", 22), new Person("Bob", 20),
				new Person("Paula", 32), new Person("Paul", 32), new Person("Jack", 2), new Person("Jack", 72),
				new Person("Jill", 11));
	}

	public static void main(String[] args) {
		Map<Boolean, List<Person>> collect = createPeople().stream()
				.collect(Collectors.partitioningBy(p -> p.getAge() % 2 == 0));
		System.out.println(collect);
	}
}