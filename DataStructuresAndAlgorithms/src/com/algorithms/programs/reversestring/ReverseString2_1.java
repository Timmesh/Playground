package com.algorithms.programs.reversestring;

public class ReverseString2_1 {
	public static void main(String[] args) {
		String reversedString = reverseString("nakul");
		System.out.println(reversedString);
	}

	private static String reverseString(String string) {
		StringBuilder builder = new StringBuilder(string);
		return builder.reverse().toString();
	}
}
