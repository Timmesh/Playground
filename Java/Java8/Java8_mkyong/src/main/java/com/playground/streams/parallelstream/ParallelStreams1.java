package com.playground.streams.parallelstream;

import java.util.stream.IntStream;

/**
 * @author USER
 * BaseStream.parallel(): A simple parallel example to print 1 to 10.
 * 
 */
public class ParallelStreams1 {
	public static void main(String[] args) {
		System.out.println("Normal...");
		IntStream range = IntStream.rangeClosed(1, 10);
		range.forEach(x -> System.out.print(x+","));

		System.out.println("Parallel...");
		IntStream range2 = IntStream.rangeClosed(1, 10);
		range2.parallel().forEach(System.out::print);
	}
}