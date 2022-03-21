package com.algorithms.interview.jpmorgan;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @author timmesh
 *
 */
public class CheckArrayPair {

	/**
	 * nums = [8, 7, 2, 5, 3, 1] target = 10
	 * 
	 * @param args
	 */
	public static void main(String[] args) {
		int[] nums = { 8, 7, 2, 5, 3, 1,9 };
		int target = 10;
		System.out.println(checkPair(nums, target));
	}

	private static List<String> checkPair(int[] nums, int target) {
		Arrays.sort(nums);
		int l = 0;
		int r = nums.length - 1;
		List<String> list = new ArrayList<>();
		while (l < r) {
			int sum = nums[l] + nums[r];
			if (sum == target) {
				list.add(nums[l] + "-" + nums[r]);
				l++;
			} else if (sum > target) {
				r--;
			} else {
				l++;
			}
		}
		return list;
	}

}
