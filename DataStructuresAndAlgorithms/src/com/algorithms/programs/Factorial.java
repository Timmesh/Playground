package com.algorithms.programs;

import java.math.BigInteger;
import java.util.stream.IntStream;
import java.util.stream.LongStream;
import java.util.stream.Stream;

public class Factorial {

	public static void main(String[] args) {
		System.out.println(factorial(10));
		System.out.println(factorialWithBigInteger(20));
		System.out.println(factorialJava8(20));
		System.out.println(factorialWithBigInteger(40));
		System.out.println(factorialJava8BigInteger(40));
	}

	private static BigInteger factorialJava8BigInteger(int i) {
		return Stream.iterate(BigInteger.ONE, j -> j.add(BigInteger.ONE)).limit(i).reduce(BigInteger.ONE,
				(x, y) -> x.multiply(y));
	}

	private static String factorialJava8(int number) {
		System.out.println(LongStream.rangeClosed(1, number).reduce(1L, (x, y) -> x * y));
		return null;
	}

	private static int factorial(int number) {
		int factorial = 1;
		for (int j = 1; j <= number; j++) {
			factorial = factorial * j;
		}
		return factorial;
	}

	private static BigInteger factorialWithBigInteger(int number) {
		BigInteger factorial = BigInteger.ONE;
		for (int j = 1; j <= number; j++) {
			factorial = factorial.multiply(BigInteger.valueOf(j));
		}
		return factorial;
	}
}
