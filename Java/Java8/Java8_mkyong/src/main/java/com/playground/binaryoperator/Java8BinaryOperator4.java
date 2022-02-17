package com.playground.binaryoperator;

import java.math.BigDecimal;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.function.BinaryOperator;

import com.playground.entities.Developer;

/**
 * This example uses BinaryOperator and a custom Comparator to find the highest
 * and lowest pay developer from a list of developers.
 *
 */
public class Java8BinaryOperator4 {

	public static void main(String[] args) {
		Developer dev1 = new Developer("jordan", BigDecimal.valueOf(9999));
		Developer dev2 = new Developer("jack", BigDecimal.valueOf(8888));
		Developer dev3 = new Developer("jaden", BigDecimal.valueOf(10000));
		Developer dev4 = new Developer("ali", BigDecimal.valueOf(2000));
		Developer dev5 = new Developer("mkyong", BigDecimal.valueOf(1));

		List<Developer> list = Arrays.asList(dev1, dev2, dev3, dev4, dev5);
		
		// 1. Create a Comparator
        Comparator<Developer> comparing = Comparator.comparing(Developer::getSalary);
        // 2. BinaryOperator with a custom Comparator
        System.out.println(find(list, BinaryOperator.maxBy(comparing)));
        System.out.println(find(list, BinaryOperator.minBy(comparing)));
        System.out.println(find(list, BinaryOperator.maxBy(Comparator.comparing(Developer::getName))));
	}

	private static Developer find(List<Developer> list, BinaryOperator<Developer> bo) {
		Developer result = null;
        for (Developer t : list) {
            if (result == null) {
                result = t;
            } else {
                result = bo.apply(result, t);
            }
        }
		return result;
	}

}
