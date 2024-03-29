package com.playground.streams.flatmap;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import com.playground.entities.Student;

/**
 * @author USER
 * 
 * Stream + Set + flatMap
 * flatMap() and Set example.
 */
public class StreamsFlatMap2 {
	public static void main(String[] args) {

		Student obj1 = new Student();
		obj1.setName("mkyong");
		obj1.addBook("Java 8 in Action");
		obj1.addBook("Spring Boot in Action");
		obj1.addBook("Effective Java (2nd Edition)");
		
		Student obj2 = new Student();
		obj2.setName("zilap");
		obj2.addBook("Learning Python, 5th Edition");
		obj2.addBook("Effective Java (2nd Edition)");
		
		List<Student> list = new ArrayList<>();
		list.add(obj1);
		list.add(obj2);
		
		/*List<String> collect = list.stream().map(x -> x.getBook()) // Stream<Set<String>>
				.flatMap(x -> x.stream()) // Stream<String>
				.distinct().collect(Collectors.toList());
		collect.forEach(x -> System.out.println(x));
		Stream<Set<String>> bookStream = list.stream().map(o -> o.getBook());
		Stream<String> flatMap = bookStream.flatMap(o->o.stream());
		Set<String> collect2 = flatMap.collect(Collectors.toSet());
		System.out.println(collect2);*/
	}
}
