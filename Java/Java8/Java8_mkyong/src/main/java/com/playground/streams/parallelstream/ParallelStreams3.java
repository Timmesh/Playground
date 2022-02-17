package com.playground.streams.parallelstream;

import java.util.stream.IntStream;

/**
 * @author USER 
 * Is Stream running in parallel mode?
 * 
 */
public class ParallelStreams3 {
	public static void main(String[] args) {

		System.out.println("Normal...");

		IntStream range = IntStream.rangeClosed(1, 10);
		System.out.println(range.isParallel()); // false
		range.forEach(System.out::print);
		System.out.println();
		System.out.println("Parallel...");

		IntStream range2 = IntStream.rangeClosed(1, 10);
		IntStream range2Parallel = range2.parallel();
		System.out.println(range2Parallel.isParallel()); // true
		range2Parallel.forEach(System.out::print);

	}
}