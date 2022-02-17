package com.playground.streams.flatmap;

import java.util.Arrays;
import java.util.List;
import java.util.OptionalInt;
import java.util.function.IntPredicate;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * @author USER
 * 
 * Stream + Primitive + flatMapToInt
 * flatMap() and Set example.
 */
public class StreamsFlatMap3 {
	public static void main(String[] args) {
        int[] intArray = {1, 2, 3, 4, 5, 6};
        IntStream stream = Arrays.stream(intArray);
        stream.forEach(x -> System.out.println(x));
        //1. Stream<int[]>
        Stream<int[]> streamArray = Stream.of(intArray);
        //2. Stream<int[]> -> flatMap -> IntStream
        IntStream intStream = streamArray.flatMapToInt(x -> Arrays.stream(x));
        intStream.forEach(x -> System.out.println(x));
        
        
    }
}
