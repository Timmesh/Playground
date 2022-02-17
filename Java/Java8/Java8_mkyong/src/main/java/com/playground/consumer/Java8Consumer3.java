package com.playground.consumer;

import java.util.Arrays;
import java.util.List;

/**
 * Higher Order Function.
 */
public class Java8Consumer3 {
	public static void main(String[] args) {
		List<String> list = Arrays.asList("a", "ab", "abc");
		list.forEach(e -> System.out.println(e.length()));
	}

}
