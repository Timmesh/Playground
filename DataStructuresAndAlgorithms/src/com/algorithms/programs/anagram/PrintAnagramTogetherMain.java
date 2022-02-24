package com.algorithms.programs.anagram;

import java.util.Collection;
import java.util.List;

/**
 * @author timmesh 
 * Time Complexity: O(MN)
 */
public class PrintAnagramTogetherMain {
	public static void main(String[] args) {
		String arr[] = { "cat", "dog", "tac", "god", "act" };
		Collection<List<String>> collect = getAnagramsTogether(arr);
		System.out.println(collect);
	}

	private static Collection<List<String>> getAnagramsTogether(String[] arr) {
		
	}
}
