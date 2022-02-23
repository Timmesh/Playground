package com.playground;

import java.util.Arrays;
import java.util.List;

/**
 * @author USER Grouping the people based on their names.
 */
public class BasicReduce {

	public static void main(String[] args) {
		List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
		System.out.println(numbers.stream().mapToInt(i->i).max());
		System.out.println(numbers.stream().mapToInt(i->i).reduce(0,(init,total)-> init+total));
		System.out.println(numbers.stream().mapToInt(i->i).sum());
		System.out.println(numbers.stream().mapToInt(i->i).min());
	}
}