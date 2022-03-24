package com.utils;

import java.util.Arrays;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * @author USER
 * 
 * 
 */
public class StreamToArray {
	public static void main(String[] args) {
		String lines = "I Love Java 8 Stream!";

		// split by space, uppercase, and convert to Array
		String[] result = Arrays.stream(lines.split("\\s+")).map(String::toUpperCase).toArray(String[]::new);
		for (String s : result) {
			System.out.println(s);
		}

		int[] num = { 1, 2, 3, 4, 5 };

		Integer[] result1 = Arrays.stream(num).map(x -> x * 2).boxed().toArray(Integer[]::new);
		System.out.println(Arrays.asList(result1));

		// IntStream -> int[]
		int[] stream1 = IntStream.rangeClosed(1, 5).toArray();
		System.out.println(Arrays.toString(stream1));

		// Stream<Integer> -> int[]
		Stream<Integer> stream2 = Stream.of(1, 2, 3, 4, 5);
		int[] result3 = stream2.mapToInt(x -> x).toArray();
		System.out.println(Arrays.toString(result3));
	}
}