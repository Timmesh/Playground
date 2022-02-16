package com.playground.streams.flatmap;

import java.util.Arrays;
import java.util.stream.Stream;

/**
 * @author USER
 *
 *         A List of Strings to Uppercase
 */
public class StreamsFlatMap1 {
	public static void main(String[] args) {
		// Stream + String[] + flatMap
		// Here print an empty result, because filter() has no idea how to filter a stream of String[].
		String[][] data = new String[][] { { "a", "b" }, { "c", "d" }, { "e", "f" } };
		// Stream<String[]>
		Stream<String[]> temp = Arrays.stream(data);
		// filter a stream of string[], and return a string[]?
		Stream<String[]> stream = temp.filter(x -> "a".equals(x.toString()));
		stream.forEach(System.out::println);

		// Using FlatMap
		// Stream<String[]>
		Stream<String[]> temp2 = Arrays.stream(data);
        Stream<String> stringStream = temp2.flatMap(x -> Arrays.stream(x));
        Stream<String> stream2 = stringStream.filter(x -> "a".equals(x.toString()));
        stream2.forEach(System.out::println);
        
        /*Stream<String> stream = Arrays.stream(data)
        	.flatMap(x -> Arrays.stream(x))	
        	.filter(x -> "a".equals(x.toString()));*/
//        Stream<String> flatMap = Arrays.stream(data).flatMap(x->Arrays.stream(x));
	}
}
