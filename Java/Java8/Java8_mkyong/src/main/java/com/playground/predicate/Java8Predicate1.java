package com.playground.predicate;

import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;

/**
 */
public class Java8Predicate1 {
	public static void main(String[] args) {
		List<Integer> list = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
		List<Integer> collect = list.stream().filter(e -> e > 5).collect(Collectors.toList());
		System.out.println(collect);

		List<Integer> collect2 = list.stream().filter(e -> e > 5 && e < 8).collect(Collectors.toList());
		System.out.println(collect2);

		Predicate<Integer> numberGreaterThan5 = x -> x > 5;
		Predicate<Integer> numberLessThan8 = x -> x < 8;
		List<Integer> collect3 = list.stream().filter(numberGreaterThan5.and(numberLessThan8))
				.collect(Collectors.toList());
		System.out.println(collect3);

	}
}
