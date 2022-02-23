package com.playground;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import com.playground.entity.Person;

/**
 * @author USER Grouping the people based on their names.
 */
public class GroupingByImp {
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
		// Imperative Style
		Map<String, List<Person>> map = new HashMap<String, List<Person>>();
		for (Person person : createPeople()) {
			List<Person> persons = map.get(person.getName());
			if (persons == null) {
				persons = new ArrayList<Person>();
			}
			persons.add(person);
			map.put(person.getName(), persons);
		}
		System.out.println("Imperative Style" + map);

		// Functional Style
		Map<String, List<Person>> map2 = createPeople().stream().collect(Collectors.groupingBy(p -> p.getName()));
		System.out.println("Functional Style" + map2);
		Map<String, List<Person>> map3 = createPeople().stream().collect(Collectors.groupingBy(Person::getName));
		System.out.println("Functional Style" + map3);

		Map<String, List<Person>> groupPeopleWithGenderByName = createPeopleWithGender().stream()
				.collect(Collectors.groupingBy(Person::getName));
		System.out.println("groupPeopleWithGenderByName" + groupPeopleWithGenderByName);

		Map<String, List<Person>> groupPeopleWithGenderByGender = createPeopleWithGender().stream()
				.collect(Collectors.groupingBy(Person::getGender));
		System.out.println("groupPeopleWithGenderByGender" + groupPeopleWithGenderByGender);

		// Get Age By Name
		Map<String, List<Integer>> map4 = createPeople().stream().collect(
				Collectors.groupingBy(p -> p.getName(), Collectors.mapping(Person::getAge, Collectors.toList())));
		System.out.println("Get Age By Name" + map4);

		// Get Age By Gender
		Map<String, List<Integer>> getAgeByGender = createPeopleWithGender().stream().collect(
				Collectors.groupingBy(Person::getGender, Collectors.mapping(Person::getAge, Collectors.toList())));
		System.out.println("getAgeByGender" + getAgeByGender);

		// Get AgeAndGender By Gender
		Map<String, List<String>> getAgeByGender2 = createPeopleWithGender().stream().collect(
				Collectors.groupingBy(Person::getGender, Collectors.mapping(Person->Person.getAge()+Person.getGender(), Collectors.toList())));
		System.out.println("getAgeByGender2" + getAgeByGender2);
		
		// Count the number of people
		Map<Object, Long> countByName = createPeople().stream()
				.collect(Collectors.groupingBy(p -> p.getName(), Collectors.counting()));
		System.out.println("countByName" + countByName);

		Map<Object, Long> countByGender = createPeopleWithGender().stream()
				.collect(Collectors.groupingBy(Person::getGender, Collectors.counting()));
		System.out.println("countByGender" + countByGender);

		// Count the number of people
		Map<Object, Integer> countByNameWithInt = createPeople().stream().collect(Collectors
				.groupingBy(p -> p.getName(), Collectors.collectingAndThen(Collectors.counting(), Long::intValue)));
		System.out.println(countByNameWithInt);
		

		
		// Filtering by age- Introduced in JAVA 9
		Map<String, List<Person>> filtering = createPeopleWithGender().stream()
	            .collect(Collectors.groupingBy(Person::getName,
	                    Collectors.filtering(e -> e.getAge() > 30, Collectors.toList())));
		System.out.println("Filtering"+filtering);
		
	}
}