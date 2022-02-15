package com.playground.unaryoperator;

import java.util.function.UnaryOperator;

/**
 * Chain UnaryOperator
 */
public class Java8UnaryOperator3 {
	public static void main(String[] args) {
		UnaryOperator<Integer> operator = u -> u + 2;
		UnaryOperator<Integer> operator2 = u -> u * 2;
		System.out.println(operator.andThen(operator2).apply(15));
	}
}
