package com.playground.util;

import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

/**
 * @author USER 
 * 
 */
public class CharacterArray {
	public static void main(String[] args) {
		String sorted = "GGAA".codePoints().mapToObj(Character::toString).sorted().collect(Collectors.joining(""));
		System.out.println(sorted);
		Map<String, Long> mapOfCharCount = "AGAE".codePoints().mapToObj(Character::toString)
				.collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
		System.out.println(mapOfCharCount);
		Map<String, Integer> collect = "GGAA".codePoints().mapToObj(Character::toString).collect(Collectors
				.groupingBy(Function.identity(), Collectors.collectingAndThen(Collectors.counting(), Long::intValue)));
		System.out.println(collect);
	}
}