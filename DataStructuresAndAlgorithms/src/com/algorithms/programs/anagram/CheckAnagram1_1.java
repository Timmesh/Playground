package com.algorithms.programs.anagram;

/**
 * Method 1.1: count characters using one array
 * 
 * Time Complexity: O(n)
 * 
 * 
 * This method assumes that the set of possible characters in both strings is
 * small. In the following implementation, it is assumed that the characters are
 * stored using 8 bit and there can be 256 possible characters.
 * 
 * 1. Create count arrays of size 256 for both strings. Initialize all values in
 * count arrays as 0. 2. Iterate through every character of both strings and
 * increment the count of character in the corresponding count arrays. 3.
 * Compare count arrays. If both count arrays are same, then return true.
 * 
 */
public class CheckAnagram1_1 {

	static int NO_OF_CHARS = 256;

	public static void main(String[] args) {
		System.out.println("isAnagram: " + checkAnagram("GGGV", "VVGG"));
	}

	private static boolean checkAnagram(String string, String string2) {
		if (string.length() != string2.length())
			return false;
		int[] count = new int[NO_OF_CHARS];
		char[] charArray = string.toCharArray();
		char[] charArray2 = string2.toCharArray();
		// For each character in input strings,
		// increment count in the corresponding
		// count array
		for (int i = 0; i < charArray.length; i++) {
			count[charArray[i] - 'A']++;
			count[charArray2[i] - 'A']--;
		}
//		Arrays.stream(count).boxed().forEach(System.out::println);
		// See if there is any non-zero
		// value in count array
		for (int i = 0; i < NO_OF_CHARS; i++) {
			if (count[i] != 0) {
				return false;
			}
		}
		return true;
	}

}
