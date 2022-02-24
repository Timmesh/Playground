package com.algorithms.programs.reversestring;

/**
 * @author timmesh
 *
 */
public class ReverseStringMain {

	public static void main(String[] args) {
		String reversedString = reverseString("nakul");
		System.out.println(reversedString);
	}

	private static String reverseString(String string) {
		String reverseString = "";
		for (int i = 0; i < string.toCharArray().length; i++) {
			char charAt = string.charAt(i);
			reverseString =  charAt + reverseString;
		}
		return reverseString;
	}

}
