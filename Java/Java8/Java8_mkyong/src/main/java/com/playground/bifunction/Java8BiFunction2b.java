package com.playground.bifunction;

import java.util.function.BiFunction;
import java.util.function.Function;

/**
 * @author USER This example converts the above program into a method that
 *         accepts BiFunction and Function as arguments and chains it together.
 */
public class Java8BiFunction2b {

	public static void main(String[] args) {

		String result = powToString(2, 4, (a1, a2) -> Math.pow(a1, a2), (r) -> "Result : " + String.valueOf(r));

		System.out.println(result); // Result : 16.0

	}

	public static <R> R powToString(Integer a1, Integer a2, BiFunction<Integer, Integer, Double> func,
			Function<Double, R> func2) {

		return func.andThen(func2).apply(a1, a2);

	}

	/**
	 *  This method converts the above method into a generic method:
	 * @param a1
	 * @param a2
	 * @param func
	 * @param func2
	 * @return
	 */
	public static <A1, A2, R1, R2> R2 convert(
			A1 a1, A2 a2, BiFunction<A1, A2, R1> func, Function<R1, R2> func2) {

		return func.andThen(func2).apply(a1, a2);

	}
}
