package com.playground.util;

import java.util.stream.Stream;

/**
 * @author
 */
public class StreamsFibonacci {

	public static void main(String[] args) {

		// A classic Fibonacci example.
		Stream.iterate(new int[] { 0, 1 }, n -> new int[] { n[1], n[0] + n[1] }).limit(20).map(n -> n[0])
				.forEach(x -> System.out.println(x));

		// Sum all the Fibonacci values.
		int sum = Stream.iterate(new int[] { 0, 1 }, n -> new int[] { n[1], n[0] + n[1] }).limit(10).map(n -> n[0]) // Stream<Integer>
				.mapToInt(n -> n).sum();
		System.out.println(sum);
	}

}
