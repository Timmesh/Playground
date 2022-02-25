package com.algorithms.programs;

import java.math.BigInteger;
import java.util.stream.Stream;

public class FibonacciNumbers {

	public static void main(String[] args) {
		// it uses a two-element array
		Stream.iterate(new int[] { 0, 1 }, l -> new int[] { l[1], l[0] + l[1] }).limit(10)
				.forEach(s -> System.out.println(s[0]));
		System.out.println();
		// .limit(92) as we can't evaluate more elements using long values.
		Stream.iterate(new long[] { 0, 1 }, l -> new long[] { l[1], l[0] + l[1] }).limit(92)
				.forEach(s -> System.out.println(s[0]));
		System.out.println();
		// That'll run until you haven't enough memory to represent the next value.
		Stream.iterate(new BigInteger[] { BigInteger.ZERO, BigInteger.ONE },
				b -> new BigInteger[] { b[1], b[0].add(b[1]) }).limit(100).forEach(b -> System.out.println(b[0]));
		// Find 4th Fibonacci searies.
		Stream.iterate(new int[] { 0, 1 }, i -> new int[] { i[1], i[0] + i[1] }).limit(4).skip(3)
				.forEach(i -> System.out.println(i[0]));

	}

}
