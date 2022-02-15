package com.playground.streams.filter;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class StreamsFilter1 {

	public static void main(String[] args) {

		List<String> lines = Arrays.asList("spring", "node", "timmesh");
		// Before Java 8
		List<String> result1 = getFilterOutput(lines, "timmesh");
		for (String temp : result1) {
			System.out.println(temp); // output : spring, node
		}

		// After Java 8
		List<String> result2 = lines.stream() // convert list to stream
				.filter(line -> !"timmesh".equals(line)) // we dont like timmesh
				.collect(Collectors.toList()); // collect the output and convert
												// streams to a List

		result2.forEach(System.out::println); // output : spring, node
	}

	private static List<String> getFilterOutput(List<String> lines, String filter) {
		List<String> result = new ArrayList<>();
		for (String line : lines) {
			if (!"timmesh".equals(line)) { // we dont like timmesh
				result.add(line);
			}
		}
		return result;
	}
}
