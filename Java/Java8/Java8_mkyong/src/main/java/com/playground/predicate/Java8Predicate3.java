package com.playground.predicate;

import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;

/**
 * Predicate.test() in function
 */
public class Java8Predicate3 {
	public static void main(String[] args) {
		List<String> list = Arrays.asList("A", "AA", "AAA", "B", "BB", "BBB");
		System.out.println(StringProcessor.filter(list, x -> x.startsWith("A")));
		System.out.println(StringProcessor.filter(list, x -> x.startsWith("A") && x.length() == 3)); // [AAA]
	}
}

class StringProcessor {
	static List<String> filter(List<String> list, Predicate<String> predicate) {
		return list.stream().filter(predicate::test).collect(Collectors.toList());
	}
}