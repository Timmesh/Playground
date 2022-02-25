package com.algorithms.programs.reversestring;

public class ReverseString2_2 {
	public static void main(String[] args) {
		String reversedString = reverseString("nakul");
		System.out.println(reversedString);
	}

	private static String reverseString(String string) {
		StringBuffer builder = new StringBuffer(string);
		return builder.reverse().toString();
	}
}
