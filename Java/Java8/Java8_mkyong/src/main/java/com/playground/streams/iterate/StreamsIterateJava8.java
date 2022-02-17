package com.playground.streams.iterate;

import java.util.stream.Stream;

/**
 * @author 
 */
public class StreamsIterateJava8 {

	public static void main(String[] args) {

		Stream.iterate(0, n -> n + 1).limit(10).forEach(x -> System.out.println(x));

		// Stream of odd numbers only.
		Stream.iterate(0, n -> n + 1).filter(x -> x % 2 != 0) // odd
				.limit(10).forEach(x -> System.out.println(x));

		// A classic Fibonacci example.
		Stream.iterate(new int[] { 0, 1 }, n -> new int[] { n[1], n[0] + n[1] })
				.limit(20).map(n -> n[0])
				.forEach(x -> System.out.print(x+" "));
		
		// Sum all the Fibonacci values. 
		int sum = Stream.iterate(new int[] { 0, 1 }, n -> new int[] { n[1], n[0] + n[1] })
				.limit(10)
				.map(n -> n[0]) // Stream<Integer>
				.mapToInt(n -> n)
				.sum();
		System.out.println(sum);
	}
}
