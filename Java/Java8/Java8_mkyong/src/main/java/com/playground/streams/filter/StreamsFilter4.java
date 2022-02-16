package com.playground.streams.filter;

import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

public class StreamsFilter4 {

	public static void main(String[] args) {
		List<String> asList = Arrays.asList("java", "python", "node", null, "ruby", null, "php");
		// List<String> result = language.collect(Collectors.toList());
		List<String> result = asList.stream().filter(x -> x != null).collect(Collectors.toList());
		result.forEach(System.out::println);
		List<String> result2 =
				asList.stream().filter(Objects::nonNull).collect(Collectors.toList());
		result2.forEach(System.out::println);
	}
}
