package com.utils;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class ArrayUtil {

	public static void main(String[] args) {
		int[] intArray = { 1, 2, 3, 4, 5, 6, 7 };
		Integer[] integerArray = Arrays.stream(intArray).boxed().toArray(Integer[]::new);
		Integer[] integerArray2 = IntStream.of(intArray).boxed().toArray(Integer[]::new);
		System.out.println(integerArray);
		System.out.println(integerArray2);

		// To boxed list
		List<Integer> integerList = Arrays.stream(intArray).boxed().collect(Collectors.toList());
		List<Integer> integerList2 = IntStream.of(intArray).boxed().collect(Collectors.toList());
		System.out.println(integerList);
		System.out.println(integerList2);
	}

}
