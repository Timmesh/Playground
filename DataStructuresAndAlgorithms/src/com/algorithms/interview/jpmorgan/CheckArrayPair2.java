package com.algorithms.interview.jpmorgan;

import java.util.HashSet;

/**
 * @author timmesh
 *
 */
public class CheckArrayPair2 {

	/**
	 * nums = [8, 7, 2, 5, 3, 1] target = 10
	 * 
	 * @param args
	 */
	public static void main(String[] args) {
		int[] nums = { 2, 7, 2, 5, 3, 1 };
		int target = 4;
		StringBuffer sb = new StringBuffer();
		HashSet<Integer> s = new HashSet<>();
		for (int i = 0; i < nums.length; i++) {
			int value = target - nums[i];
			if (s.contains(value)) {
				sb.append("(");
				sb.append(nums[i] + "," + value);
				sb.append(")\n");
			}
			s.add(nums[i]);
		}
		System.out.println(sb.toString());
	}

}
