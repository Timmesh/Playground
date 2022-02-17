package com.playground.bifunction;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.BiFunction;

/**
 * @author USER Filtering a List by some conditions.
 */
public class Java8BiFunction4 {

	public static void main(String[] args) {

		Java8BiFunction4 obj = new Java8BiFunction4();

		List<String> list = Arrays.asList("node", "c++", "java", "javascript");

		// BiFunction<String, Integer, String> filterByLengthCondition = (t, u)
		// -> obj.filterByLength(t, u);
		BiFunction<String, Integer, String> filterByLengthCondition = obj::filterByLength;
		List<String> result = obj.filterList(list, 3, filterByLengthCondition);

		System.out.println(result); // [node, java, javascript]

		BiFunction<String, Integer, String> filterByLengthCondition2 = (l1, size) -> {
			if (l1.length() > size) {
				return l1;
			} else {
				return null;
			}
		};
		List<String> result1 = obj.filterList(list, 3, filterByLengthCondition2);

		System.out.println(result1); // [node, java, javascript]

		BiFunction<String, String, String> filterByStartCharCondition = (l1, condition) -> {
			if (l1.startsWith(condition)) {
				return l1;
			} else {
				return null;
			}
		};
		List<String> result2 = obj.filterList(list, "c", filterByStartCharCondition);

		System.out.println(result2); // [c++]

		List<Integer> number = Arrays.asList(1, 2, 3, 4, 5);

		BiFunction<Integer, Integer, Integer> modCondition = (l1, condition) -> {
			if (l1 % condition == 0) {
				return l1;
			} else {
				return null;
			}
		};
		List<Integer> result3 = obj.filterList(number, 2, modCondition);

		System.out.println(result3); // [2, 4]

	}

	public String filterByLength(String str, Integer size) {
		if (str.length() > size) {
			return str;
		} else {
			return null;
		}
	}

	public <T, U, R> List<R> filterList(List<T> list1, U value, BiFunction<T, U, R> condition) {

		List<R> result = new ArrayList<>();

		for (T t : list1) {
			R apply = condition.apply(t, value);
			if (apply != null) {
				result.add(apply);
			}
		}

		return result;

	}

}
