package com.playground.streams.reduce;

import java.util.Arrays;

/**
 * @author USER the Stream.reduce() combine elements of a stream and produces a
 *         single value.
 * 
 */
public class StreamsReduce1 {
	public static void main(String[] args) {
		// Before java 8
		int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
		int sum = 0;
		for (int i : numbers) {
			sum += i;
		}
		System.out.println("sum : " + sum); // 55
		// After Java 8
		int sum1 = Arrays.stream(numbers).reduce(0, (a, b) -> a + b);
		System.out.println("sum : " + sum1); // 55
		
		int sum2 = Arrays.stream(numbers).reduce(0, Integer::sum); // 55
		System.out.println("sum : " + sum2); // 55
	}
}