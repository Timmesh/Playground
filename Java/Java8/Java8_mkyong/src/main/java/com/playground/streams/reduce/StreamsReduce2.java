package com.playground.streams.reduce;

import java.util.Arrays;

/**
 * @author USER the Stream.reduce() combine elements of a stream and produces a
 *         single value.
 * 
 */
public class StreamsReduce2 {
	public static void main(String[] args) {
		// Math operations.
		int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

		int sum = Arrays.stream(numbers).reduce(0, (a, b) -> a + b);    // 55
		int sum2 = Arrays.stream(numbers).reduce(0, Integer::sum);      // 55

		int sum3 = Arrays.stream(numbers).reduce(0, (a, b) -> a - b);   // -55
		int sum4 = Arrays.stream(numbers).reduce(0, (a, b) -> a * b);   // 0, initial is 0, 0 * whatever = 0
		int sum5 = Arrays.stream(numbers).reduce(0, (a, b) -> a / b);   // 0
		
		// Max and Min.
		int max = Arrays.stream(numbers).reduce(0, (a, b) -> a > b ? a : b);  // 10
		int max1 = Arrays.stream(numbers).reduce(0, Integer::max);            // 10

		int min = Arrays.stream(numbers).reduce(0, (a, b) -> a < b ? a : b);  // 0
		int min1 = Arrays.stream(numbers).reduce(0, Integer::min);            // 0
		
	}
}