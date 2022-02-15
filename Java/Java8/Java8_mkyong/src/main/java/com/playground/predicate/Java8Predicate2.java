package com.playground.predicate;

import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;

/**
 */
public class Java8Predicate2 {
	public static void main(String[] args) {
		Predicate<String> lengthIs3 = x -> x.length() == 3;
		Predicate<String> startWithA = x -> x.startsWith("A");

		List<String> list = Arrays.asList("A", "AA", "AAA", "B", "BB", "BBB");

		List<String> collect = list.stream().filter(startWithA.or(lengthIs3)).collect(Collectors.toList());
		System.out.println(collect);

		System.out.println(lengthIs3.test("Timm"));
		
		List<String> collect2 = list.stream().filter(startWithA.negate()).collect(Collectors.toList());
		System.out.println(collect2);
		
	}
}
