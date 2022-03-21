package com.algorithms.programs.reversestring;

/**
 * @author timmesh
 *
 */
public class ReverseStringMain {

	public static void main(String[] args) {
		String reversedString = reverseString("nakul");
		System.out.println(reversedString);
		System.out.println(reverseStringUsingStream("nakul"));
	}

	private static String reverseString(String string) {
		String reverseString = "";
		for (int i = 0; i < string.toCharArray().length; i++) {
			char charAt = string.charAt(i);
			reverseString =  charAt + reverseString;
		}
		return reverseString;
	}
	
	private static String reverseStringUsingStream(String string) {
		return string.codePoints().mapToObj(Character::toString).reduce("", (i,j) -> j+i);
	}

}
