package com.utils;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @author USER
 * sort list with stream.sorted()
 * 
 */
public class StreamSort1 {
	public static void main(String[] args) {
		List<String> list = Arrays.asList("9", "A", "Z", "1", "B", "Y", "4", "a", "c");
		/* 
		List<String> sortedList = list.stream()
			.sorted(Comparator.naturalOrder())
			.collect(Collectors.toList());

        List<String> sortedList = list.stream()
			.sorted((o1,o2)-> o1.compareTo(o2))
			.collect(Collectors.toList());
		 */
		List<String> sortedList = list.stream().sorted().collect(Collectors.toList());
		System.out.println(sortedList);
		// Sort a List with Comparator.reverseOrder()
		
		/*
		List<String> sortedList = list.stream()
			.sorted((o1,o2)-> o2.compareTo(o1))
			.collect(Collectors.toList());
		*/
		
        List<String> reverseSortedList = list.stream()
			.sorted(Comparator.reverseOrder())
			.collect(Collectors.toList());
        System.out.println(reverseSortedList);
        
        
	}
}