package com.playground.util;

import java.util.Arrays;
import java.util.List;

/**
 * @author USER 
 * 
 * 
 */
public class StreamsPeek {
	public static void main(String[] args) {
		List<String> l = Arrays.asList("A", "B", "C", "D");

		long count = l.stream().peek(System.out::println).count();

		System.out.println(count); // 4
		
		// From Java 9 the peek may not work.
		// https://mkyong.com/java8/java-8-stream-the-peek-is-not-working-with-count/
	}
}