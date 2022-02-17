package com.playground.streams.reduce;

import java.util.Arrays;

/**
 * @author USER the Stream.reduce() combine elements of a stream and produces a
 *         single value.
 * 
 */
public class StreamsReduce3 {
	public static void main(String[] args) {
		String[] strings = { "a", "b", "c", "d", "e" };

		// |a|b|c|d|e , the initial | join is not what we want
		String reduce = Arrays.stream(strings).reduce("", (a, b) -> a + "|" + b);
		System.out.println(reduce);
//		System.out.println(Arrays.stream(strings).reduce("", (a,b)->a +","+b));
		
		// a|b|c|d|e, filter the initial "" empty string
		String reduce2 = Arrays.stream(strings).reduce("", (a, b) -> {
			if (!"".equals(a)) {
				return a + "|" + b;
			} else {
				return b;
			}
		});
		System.out.println(reduce2);
		// a|b|c|d|e , better uses the Java 8 String.join :)
		String join = String.join("|", strings);
		System.out.println(join);
	}
}