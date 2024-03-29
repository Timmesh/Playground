package com.utils;

import java.io.IOException;
import java.util.Scanner;

/**
 * @author timmesh
 *
 */
public class CommandLineInput {
	public static void main(String[] args) {
		// Using Scanner for Getting Input from User
		Scanner in = new Scanner(System.in);

		String s = in.nextLine();
		System.out.println("You entered string " + s);

		int a = in.nextInt();
		System.out.println("You entered integer " + a);

		float b = in.nextFloat();
		System.out.println("You entered float " + b);

		// closing scanner
		in.close();
	}
}
