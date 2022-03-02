package com.utils;

import java.io.IOException;

/**
 * @author timmesh
 *
 */
public class EnterKeyInput {
	public static void main(String[] args) {
		System.out.println("Press ENTER Key");
		try {
			System.in.read();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
