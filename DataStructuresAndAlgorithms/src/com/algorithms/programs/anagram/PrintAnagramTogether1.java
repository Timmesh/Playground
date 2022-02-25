package com.algorithms.programs.anagram;

import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;

/**
 * @author timmesh 
 * Time Complexity: O(MNLogN)
 */
public class PrintAnagramTogether1 {
	public static void main(String[] args) {
		String arr[] = { "cat", "dog", "tac", "god", "act" };
		Collection<List<String>> collect = getAnagramsTogether(arr);
		System.out.println(collect);
	}

	private static Collection<List<String>> getAnagramsTogether(String[] arr) {
		Map<Object, List<String>> collect = Arrays.stream(arr).map(str -> {
			char[] charArray = str.toCharArray();
			Arrays.sort(charArray);
			return new String[] { str, new String(charArray) };
		}).collect(Collectors.groupingBy(s -> s[1],
				Collectors.mapping((Function<String[], String>) s -> s[0], Collectors.toList())));
		return collect.values();
	}
}
