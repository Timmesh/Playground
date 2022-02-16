package com.playground.streams.parallelstream;

import java.util.ArrayList;
import java.util.List;

/**
 * @author USER BaseStream.parallel(): A simple parallel example to print 1 to
 *         10.
 * 
 */
public class ParallelStreams2 {
	public static void main(String[] args) {
		System.out.println("Normal...");
		List<String> alpha = getData();
		alpha.stream().forEach(System.out::print);
		System.out.println();
		System.out.println("Parallel...");
		List<String> alpha2 = getData();
		alpha2.parallelStream().forEach(System.out::print);
	}

	private static List<String> getData() {
		List<String> alpha = new ArrayList<>();
		int n = 97; // 97 = a , 122 = z
		while (n <= 122) {
			char c = (char) n;
			alpha.add(String.valueOf(c));
			n++;
		}
		return alpha;
	}
}