package com.playground.util;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

/**
 * @author USER he findFirst() returns the first element from a Stream, while
 *         findAny() returns any element from a Stream..
 * 
 */
public class StreamsFind {
	public static void main(String[] args) {
		List<Integer> list = Arrays.asList(1, 2, 3, 2, 1);
		Optional<Integer> first = list.stream().findFirst();
		if (first.isPresent()) {
			Integer result = first.get();
			System.out.println(result); // 1
		} else {
			System.out.println("no value?");
		}
		Optional<Integer> first2 = list.stream().filter(x -> x > 1).findFirst();
		if (first2.isPresent()) {
			System.out.println(first2.get()); // 2
		} else {
			System.out.println("no value?");
		}
		List<String> list2 = Arrays.asList("node", "java", "python", "ruby");

        Optional<String> result = list2.stream()
                .filter(x -> !x.equalsIgnoreCase("node"))
                .findFirst();

        if (result.isPresent()) {
            System.out.println(result.get()); // java
        } else {
            System.out.println("no value?");
        }
        
        // Find Any
        List<Integer> list3 = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        Optional<Integer> any = list3.stream().filter(x -> x > 1).findAny();
        if (any.isPresent()) {
            Integer result1 = any.get();
            System.out.println(result1);
        }
	}
}