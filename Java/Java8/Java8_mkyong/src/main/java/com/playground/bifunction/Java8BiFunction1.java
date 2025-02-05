package com.playground.bifunction;

import java.util.Arrays;
import java.util.List;
import java.util.function.BiFunction;

/**
 * @author USER
 * 
 * BiFunction<T, U, R> : This example takes two Integers and returns an Integer, Double or List
 * T � Type of the first argument to the function.
 * U � Type of the second argument to the function.
 * R � Type of the result of the function.
 */
public class Java8BiFunction1 {

    public static void main(String[] args) {
        // takes two Integers and return an Integer
        BiFunction<Integer, Integer, Integer> func = (x1, x2) -> x1 + x2;
        Integer result = func.apply(2, 3);

        System.out.println(result); // 5

        // take two Integers and return an Double
        BiFunction<Integer, Integer, Double> func2 = (x1, x2) -> Math.pow(x1, x2);

        Double result2 = func2.apply(2, 4);

        System.out.println(result2);    // 16.0

        // take two Integers and return a List<Integer>
        BiFunction<Integer, Integer, List<Integer>> func3 = (x1, x2) -> Arrays.asList(x1 + x2);

        List<Integer> result3 = func3.apply(2, 3);

        System.out.println(result3);

    }

}
