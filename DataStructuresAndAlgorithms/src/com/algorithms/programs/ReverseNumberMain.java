package com.algorithms.programs;

/**
 * @author timmesh
 *
 */
public class ReverseNumberMain {

	public static void main(String[] args) {
		System.out.println(reverseNumber(1523));

	}

	private static int reverseNumber(int number) {
		int reverse = 0;
		while (number > 0) {
			int reduce = number % 10;
			reverse = reverse * 10 + reduce;
			number = number / 10;
		}
		return reverse;
	}

}
