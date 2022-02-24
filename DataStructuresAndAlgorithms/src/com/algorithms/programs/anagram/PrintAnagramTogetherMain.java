package com.algorithms.programs.anagram;

import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

/**
 * @author timmesh 
 * Time Complexity: O(MN)
 */
public class PrintAnagramTogetherMain {
	public static void main(String[] args) {
		String arr[] = { "cat", "dog", "tac", "god", "act" };
		Collection<List<String>> collect = getAnagramsTogether(arr);
		System.out.println(collect);
	}

	private static Collection<List<String>> getAnagramsTogether(String[] arr) {
		Map<Map<String, Long>, List<String>> collect = Arrays.stream(arr)
				.collect(Collectors.groupingBy(
						(Function<String, Map<String, Long>>) s -> s.codePoints().mapToObj(Character::toString)
								.collect(Collectors.groupingBy(Function.identity(), Collectors.counting()))));
		return collect.values();

	}
}
