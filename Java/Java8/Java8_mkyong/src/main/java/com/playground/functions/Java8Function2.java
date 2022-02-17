package com.playground.functions;

import java.util.function.Function;

/**
 * @author USER
 * Chain Function<T, R> : This example chains the Function with andThen().
 */
public class Java8Function2 {

    public static void main(String[] args) {
        Function<String, Integer> func = x -> x.length();
        Function<Integer, Integer> func2 = x -> x * 2;
        Integer result = func.andThen(func2).apply("Nakul");   
        System.out.println(result);
    }
}
