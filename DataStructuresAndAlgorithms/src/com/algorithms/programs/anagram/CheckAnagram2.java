package com.algorithms.programs.anagram;

import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

/**
 *	Not Recommended.
 *
 *	Written for Interview
 */
public class CheckAnagram2 {
	public static void main(String[] args) {
		System.out.println("isAnagram: " + checkAnagram("GGVV", "GGGV"));
	}

	private static boolean checkAnagram(String string, String string2) {
		Map<String, Integer> map = string.codePoints().mapToObj(Character::toString).collect(Collectors
				.groupingBy(Function.identity(), Collectors.collectingAndThen(Collectors.counting(), Long::intValue)));
		Map<String, Integer> map2 = string2.codePoints().mapToObj(Character::toString).collect(Collectors.groupingBy(
				Function.identity(), Collectors.collectingAndThen(Collectors.counting(), i -> i.intValue())));
		return areEqual(map,map2);
	}

	private static boolean areEqual(Map<String, Integer> first, Map<String, Integer> second) {
		if (first.size() != second.size()) {
			return false;
		}
		return first.entrySet().stream().allMatch(e -> e.getValue().equals(second.get(e.getKey())));
	}
}
