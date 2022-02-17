package com.playground.streams.filter;

import java.util.Arrays;
import java.util.List;

import com.playground.entities.Person;

/**
 * @author USER
 * 2. Streams filter(), findAny() and orElse()
 *
 */
public class StreamsFilter2 {
	public static void main(String[] args) {

		List<com.playground.entities.Person> persons = Arrays.asList(new Person("mkyong", 30), new Person("jack", 20),
				new Person("lawrence", 40));
		// Before Java 8
		Person result = getStudentByName(persons, "jack");
		System.out.println(result);

		// After Java 8
		Person result1 = persons.stream() // Convert to steam
				.filter(x -> "jack".equals(x.getName())) // we want "jack" only
				.findAny() // If 'findAny' then return found
				.orElse(null); // If not found, return null

		System.out.println(result1);

		Person result2 = persons.stream().filter(x -> "ahmook".equals(x.getName())).findAny().orElse(null);

		System.out.println(result2);

		// Multiple Conditions
		Person result3 = persons.stream().filter((p) -> "jack".equals(p.getName()) && 20 == p.getAge()).findAny()
				.orElse(null);

		System.out.println("result 3 :" + result3);

		// or like this
		Person result4 = persons.stream().filter(p -> {
			if ("jack".equals(p.getName()) && 20 == p.getAge()) {
				return true;
			}
			return false;
		}).findAny().orElse(null);

		System.out.println("result 4 :" + result4);
	}

	private static Person getStudentByName(List<Person> persons, String name) {

		Person result = null;
		for (Person temp : persons) {
			if (name.equals(temp.getName())) {
				result = temp;
			}
		}
		return result;
	}
}
