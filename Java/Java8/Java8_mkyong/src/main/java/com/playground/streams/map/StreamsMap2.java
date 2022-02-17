package com.playground.streams.map;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import com.playground.entities.Staff;

/**
 * @author USER
 *
 * List of objects -> List of String Get all the name values from a list
 * of the staff objects.
 */
public class StreamsMap2 {
	public static void main(String[] args) {

		List<Staff> staff = Arrays.asList(new Staff("mkyong", 30, new BigDecimal(10000)),
				new Staff("jack", 27, new BigDecimal(20000)), new Staff("lawrence", 33, new BigDecimal(30000)));

		// Before Java 8
		List<String> result = new ArrayList<>();
		for (Staff x : staff) {
			result.add(x.getName());
		}
		System.out.println(result); // [mkyong, jack, lawrence]

		// Java 8
		List<String> collect = staff.stream().map(x -> x.getName()).collect(Collectors.toList());
		System.out.println(collect); // [mkyong, jack, lawrence]
	}
}
