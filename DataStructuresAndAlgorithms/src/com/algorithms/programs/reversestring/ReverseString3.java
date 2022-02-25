package com.algorithms.programs.reversestring;

/**
 * @author timmesh
 *
 */
public class ReverseString3 {
	public static void main(String[] args) {
		String reversedString = reverseString("nakul");
		System.out.println(reversedString);
	}

	private static String reverseString(String string) {
		char[] try1 = string.toCharArray();
		StringBuilder builder = new StringBuilder();
        for (int i = try1.length - 1; i >= 0; i--)
        	builder.append(try1[i]);
        return builder.toString();
	}
}
