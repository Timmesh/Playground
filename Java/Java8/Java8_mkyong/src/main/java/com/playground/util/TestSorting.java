package com.playground.util;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

import com.playground.entities.Developer;

/**
 */
public class TestSorting {
	public static void main(String[] args) {

		List<Developer> listDevs = getDevelopers();

		System.out.println("Before Sort");
		for (Developer developer : listDevs) {
			System.out.println(developer);
		}

		System.out.println("After Sort");

		// lambda here!
		listDevs.sort((o1, o2) -> o1.getAge() - o2.getAge());

		// java 8 only, lambda also, to print the List
		listDevs.forEach((developer) -> System.out.println(developer));
		System.out.println("Sort By Name");
		listDevs.sort((o1,o2) -> o1.getName().compareTo(o2.getName()));
		listDevs.forEach(System.out::println);
		System.out.println("Sort By Salary");
		listDevs.sort((o1,o2) -> o1.getSalary().compareTo(o2.getSalary()));
		listDevs.forEach(System.out::println);
		System.out.println("Sort By Salary Reversed");
		Comparator<? super Developer> c = (o1,o2) -> o1.getSalary().compareTo(o2.getSalary());
		listDevs.sort(c.reversed());
		listDevs.forEach(System.out::println);
		
	}

	private static List<Developer> getDevelopers() {

		List<Developer> result = new ArrayList<Developer>();

		result.add(new Developer("mkyong", new BigDecimal("70000"), 33));
		result.add(new Developer("alvin", new BigDecimal("80000"), 20));
		result.add(new Developer("jason", new BigDecimal("100000"), 10));
		result.add(new Developer("iris", new BigDecimal("170000"), 55));

		return result;

	}
}
