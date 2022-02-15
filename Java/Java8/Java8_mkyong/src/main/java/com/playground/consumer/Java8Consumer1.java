package com.playground.consumer;

import java.util.function.Consumer;

/**
 * Consumer
 */
public class Java8Consumer1 {
	public static void main(String[] args) {
		Consumer<String> print = x -> System.out.println(x);
        print.accept("java");   // java
        
		Consumer<String> print2 = System.out::println;
        print2.accept("java");   // java

	}
}
