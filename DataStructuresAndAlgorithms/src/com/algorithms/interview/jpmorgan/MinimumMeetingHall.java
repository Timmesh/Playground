package com.algorithms.interview.jpmorgan;

/**
 * @author timmesh
 * 
 * Input: lectures[][] = {{0, 5}, {1, 2}, {1, 10}} 
 * Output: 3 
 * All lectures must be held in different halls because 
 * at time instance 1 all lectures are ongoing.
 * Input: lectures[][] = {{0, 5}, {1, 2}, {6, 10}} 
 * Output: 2 
 *
 */
public class MinimumMeetingHall {
	static int MAX = 100001;

// Function to return the minimum
// number of halls required
	static int minHalls(int lectures[][], int n) {

		// Array to store the number of
		// lectures ongoing at time t
		int[] prefix_sum = new int[24];

		// For every lecture increment start
		// point s decrement (end point + 1)
		for (int i = 0; i < n; i++) {
			prefix_sum[lectures[i][0]]++;
			prefix_sum[lectures[i][1]]--;
		}

		int ans = prefix_sum[0];

		// Perform prefix sum and update
		// the ans to maximum
		for (int i = 1; i < 24; i++) {
			prefix_sum[i] += prefix_sum[i - 1];
			ans = Math.max(ans, prefix_sum[i]);
		}
		return ans;
	}

// Driver code
	public static void main(String[] args) {
		int lectures[][] = { { 0, 3 }, { 2, 3 }, { 3, 4 },{ 3, 10 } };
		int n = lectures.length;

		System.out.println(minHalls(lectures, n));
	}
}

