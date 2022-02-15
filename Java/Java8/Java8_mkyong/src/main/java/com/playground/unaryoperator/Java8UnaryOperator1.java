package com.playground.unaryoperator;

import java.util.function.Function;
import java.util.function.UnaryOperator;

/**
 * @author USER Filtering a List by some conditions.
 */
public class Java8UnaryOperator1 {

	public static void main(String[] args) {
		Function<Integer, Integer> f = x -> x+2;
		System.out.println(f.apply(10));
		
		UnaryOperator<Integer> u = x -> x+2;
		System.out.println(u.apply(10));
	}
}
