package com.algorithms.programs.anagram;

import java.util.HashMap;
import java.util.Map;

/**
 * Method 1.2:Put all characters in HashMap
 * Time Complexity: O(n)
 * 
 * Similar to CheckAnagram1_1, Using map instead of int[]
 */
public class CheckAnagram1_2 {

	public static void main(String[] args) {
		System.out.println("isAnagram: " + checkAnagram("GVCG", "VVGC"));
	}

	private static boolean checkAnagram(String string, String string2) {
		if (string.length() != string2.length())
			return false;
		Map<Integer, Integer> counter = new HashMap<Integer, Integer>();
		char[] charArray = string.toCharArray();
		char[] charArray2 = string2.toCharArray();
		// For each character in input strings,
	    // increment count in the corresponding
	    // count array
		for (int i = 0; i < charArray.length; i++) {
			Integer integer = getMapValue(counter, charArray, i);
			counter.put(charArray[i] - 'A', ++integer);
			Integer integer2 = getMapValue(counter, charArray2, i);
			counter.put(charArray2[i] - 'A', --integer2);
		}
		System.out.println(counter);
		// See if there is any non-zero
	    // value in counter Map
		return counter.values().stream().allMatch(value->value == 0);
	}

	private static Integer getMapValue(Map<Integer, Integer> counter, char[] charArray, int i) {
		Integer integer = counter.get(charArray[i] - 'A');
		if (integer == null) {
			integer = Integer.valueOf(0);
		}
		return integer;
	}

}
