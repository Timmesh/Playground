package com.playground.streams.collectors;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

/**
 * @author USER 
 * Group by a List and display the total count of it.
 * 
 */
public class StreamCollectors1 {
	public static void main(String[] args) {
		// 3 apple, 2 banana, others 1
		List<String> items = Arrays.asList("apple", "apple", "banana", "apple", "orange", "banana", "papaya");
		Map<String, Long> result = items.stream()
				.collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
		System.out.println(result);
	}
}