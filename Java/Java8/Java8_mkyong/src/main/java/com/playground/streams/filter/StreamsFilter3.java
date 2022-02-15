package com.playground.streams.filter;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

import com.playground.entities.Person;


/**
 * @author USER
 *
 * Streams filter() and map().
 */
public class StreamsFilter3 {
	public static void main(String[] args) {

        List<Person> persons = Arrays.asList(
                new Person("mkyong", 30),
                new Person("jack", 20),
                new Person("lawrence", 40)
        );

        String name = persons.stream()
                .filter(x -> "jack".equals(x.getName()))
                .map(Person::getName)                        //convert stream to String
                .findAny()
                .orElse("");

        System.out.println("name : " + name);

        List<String> collect = persons.stream()
                .map(Person::getName)
                .collect(Collectors.toList());

        collect.forEach(System.out::println);
        Optional<String> person1 = persons.stream()
                .filter(c -> c.getName().equals("jack"))
                .map(Person::getName)
                .findAny();
        // Note that it returns an Optional<String> because there may be no Person that matches "jack".
        // If you want to use a default if "jack" is not found you can use:
        String person2 = persons.stream()
                .filter(c -> c.getName().equals("jack"))
                .map(Person::getName)
                .findAny().orElse("");
	}

	
}
