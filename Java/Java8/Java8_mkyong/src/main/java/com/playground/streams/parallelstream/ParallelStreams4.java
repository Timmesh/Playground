package com.playground.streams.parallelstream;

import java.util.stream.IntStream;

/**
 * @author USER 
 * print the current thread name
 * 
 */
public class ParallelStreams4 {
	public static void main(String[] args) {
		System.out.println("Normal...");
		IntStream range = IntStream.rangeClosed(1, 10);
		range.forEach(x -> {
			System.out.println("Thread : " + Thread.currentThread().getName() + ", value: " + x);
		});
		System.out.println("Parallel...");

		IntStream range2 = IntStream.rangeClosed(1, 10);
		range2.parallel().forEach(x -> {
			System.out.println("Thread : " + Thread.currentThread().getName() + ", value: " + x);
		});
	}
}