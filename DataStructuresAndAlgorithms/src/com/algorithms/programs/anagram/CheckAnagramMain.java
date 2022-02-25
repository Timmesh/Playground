package com.algorithms.programs.anagram;

import java.util.stream.Collectors;

/**
 * @author USER
 * Time Complexity: O(nLogn)
 */
public class CheckAnagramMain {
	public static void main(String[] args) {
		System.out.println("isAnagram: " + checkAnagram("GGVV", "VVGG"));
	}

	private static boolean checkAnagram(String string, String string2) {
		String sorted = string.codePoints().mapToObj(Character::toString).sorted().collect(Collectors.joining(""));
		String sorted2 = string2.codePoints().mapToObj(Character::toString).sorted().collect(Collectors.joining());
		if (sorted.equals(sorted2))
			return true;
		return false;
	}

}
