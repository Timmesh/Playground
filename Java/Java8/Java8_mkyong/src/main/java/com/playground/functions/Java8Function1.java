package com.playground.functions;

import java.util.function.Function;

/**
 * @author USER
 *
 */
public class Java8Function1 {

	public static void main(String[] args) {
		
		String string = "Nakul";
		Function<String, Integer> withoutLambdaFunction = new Function<String, Integer>() {
			@Override
			public Integer apply(String string) {
				return string.length();
			}
		};
		System.out.println(withoutLambdaFunction.apply(string));
		
		Function<String, Integer> withLambdaFunction = x -> x.length();
		System.out.println(withLambdaFunction.apply(string));
	}

}
