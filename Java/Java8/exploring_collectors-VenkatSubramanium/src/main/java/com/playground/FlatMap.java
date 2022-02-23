package com.playground;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import com.playground.entity.Person;

/**
 * @author USER Grouping the people based on their names.
 */
public class FlatMap {
	
	public static List<Person> createPeople() {
		return Arrays.asList(new Person("Sara", 20), new Person("Sara", 22), new Person("Bob", 20),
				new Person("Paula", 32), new Person("Paul", 32), new Person("Jack", 2), new Person("Jack", 72),
				new Person("Jill", 11));
	}

	public static void main(String[] args) {
		List<Integer> integers = Arrays.asList(1, 2, 3);
		List<Integer> stream = integers.stream()
				.map(i -> i * 2) // One-to-One function
				.collect(Collectors.toList());
		// Stream<T>.map(f11) ==> Stream<R>
		System.out.println(stream);
		
		List<List<Integer>> streamOfStream = integers.stream()
				.map(i -> Arrays.asList(i - 1, i + 1)) // One to many function
				.collect(Collectors.toList());
		// Stream<T>.map(f11) ==> Stream<List<R>>		
		System.out.println(streamOfStream);
		
//		Stream
//			.Map(Function<T,R>) ===> Stream<R>
//			.flatMap(Function<T, (Iterable<R>)Stream<R>>) ===> Stream<R>
		
		List<Integer> flatMap = integers.stream()
				.flatMap(i -> Arrays.asList(i - 1, i + 1).stream()) // One to many function
				.collect(Collectors.toList());
// 		Stream<T>.map(f11) ==> Stream<List<R>>		
		System.out.println(flatMap);

		List<String> flatMap2 = createPeople().stream()
				.flatMap(p -> Stream.of(p.getName().split(""))) // One to many function
				.collect(Collectors.toList());
		System.out.println(flatMap2);
		
		Map<String, List<Object>> collect = createPeople().stream()
				.collect(Collectors.groupingBy(Person::getName,
						Collectors.mapping(p->p.getName().split(""), Collectors.toList())));
		System.out.println(collect);
		//FlatMapping not present in Java 8
		// Collect the characters of the name
		Map<String, List<Object>> collect2 = createPeople().stream()
				.collect(Collectors.groupingBy(Person::getName,
						Collectors.flatMapping(p->Stream.of(p.getName().split("")), Collectors.toList())));
		System.out.println("collect2"+collect2);

		/* 
		 * Collect the characters of the name and remove duplicates.		
		 Map<String, List<Object>> collect3 = createPeople().stream()
		.collect(Collectors.groupingBy(Person::getName,
				Collectors.flatMapping(p->Stream.of(p.getName().split("")), Collectors.toSet())));
		 */

		/*
		 * Map<String, Set<Object>> collect4 = createPeople().stream()
		 * .collect(Collectors.groupingBy(Person::getName, Collectors.mapping(p ->
		 * p.getName().toUpperCase(), Collectors.flatMapping(p -> Stream.of(((Person)
		 * p).getName().split("")), Collectors.toSet()))));
		 */
		
	}
}