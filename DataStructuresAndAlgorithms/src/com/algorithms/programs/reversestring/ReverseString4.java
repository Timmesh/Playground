package com.algorithms.programs.reversestring;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Iterator;
import java.util.stream.Collectors;

/**
 * @author timmesh
 *
 */
public class ReverseString4 {
	public static void main(String[] args) {
		String reversedString = reverseString("nakul");
		System.out.println(reversedString);
	}

	private static String reverseString(String string) {
		Iterator<String> descendingIterator = Arrays.stream(string.split(""))
				.collect(Collectors.toCollection(ArrayDeque::new)) // or LinkedList
				.descendingIterator();
		StringBuffer s = new StringBuffer();
		while(descendingIterator.hasNext()) {
			s.append(descendingIterator.next());
		}
		return s.toString();
	}
}
