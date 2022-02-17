package com.playground.binaryoperator;

import java.util.function.IntBinaryOperator;

/**
 * This example simulates a stream.reduce() to sum all the Integer.
 */
public class Java8BinaryOperator3 {
	public static void main(String[] args) {
		int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
		IntBinaryOperator binaryOperator = (a, b) -> a + b;
		int result = 0;
		for (int i : numbers) {
			result = binaryOperator.applyAsInt(result, i);
		}
		System.out.println(result);
	}

}
