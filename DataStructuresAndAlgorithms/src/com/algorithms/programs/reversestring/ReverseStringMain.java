package com.algorithms.programs.reversestring;

import java.util.Arrays;

import com.sun.tools.javac.code.Attribute.Array;

/**
 * @author timmesh
 *
 */
public class ReverseStringMain {

	public static void main(String[] args) {
		System.out.println(reverseString("nakul"));
		System.out.println(reverseStringUsingStream("nakul"));
		System.out.println(reverseStringUsingStreamJava8("nakul"));
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
	
	private static String reverseStringUsingStreamJava8(String string) {
		return Arrays.stream(string.split("")).reduce("", (i,j) -> j + i);
	}

}
