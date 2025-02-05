package com.algorithms.analysis;

import java.util.HashMap;
import java.util.Map;

/**
 * This class demonstrates four different implementations of Fibonacci number calculation:
 * 1. Recursive (Without Memoization)
 * 2. Recursive (With Memoization)
 * 3. Iterative (Dynamic Programming with Array)
 * 4. Optimized Iterative (Constant Space)
 */
public class FibonacciImplementations {

    /**
     * 1. Recursive Implementation (Without Memoization)
     *
     * - Approach: The simplest form of recursion.
     * - Space Complexity: O(n) (due to recursion stack).
     * - Auxiliary Space: O(n) (each recursive call adds a stack frame).
     * - Time Complexity: O(2^n) (due to repeated subproblems).
     *
     * Drawback: Very slow for large n due to repeated calculations.
     */
    public static int fibRecursive(int n) {
        if (n <= 1) {
            return n;
        }
        return fibRecursive(n - 1) + fibRecursive(n - 2);
    }

    /**
     * 2. Recursive Implementation (With Memoization)
     *
     * - Approach: Uses a HashMap to store previously calculated Fibonacci numbers.
     * - Space Complexity: O(n) (due to recursion stack and HashMap storage).
     * - Auxiliary Space: O(n) (recursion stack depth up to n).
     * - Time Complexity: O(n) (each value is calculated once).
     *
     * Advantage: Avoids repeated calculations by caching results.
     */
    private static Map<Integer, Integer> memo = new HashMap<>();
    public static int fibMemoization(int n) {
        if (memo.containsKey(n)) {
            return memo.get(n);
        }
        if (n <= 1) {
            return n;
        }
        int result = fibMemoization(n - 1) + fibMemoization(n - 2);
        memo.put(n, result);
        return result;
    }

    /**
     * 3. Iterative Implementation (Dynamic Programming with Array)
     *
     * - Approach: Bottom-up approach using an array to store intermediate results.
     * - Space Complexity: O(n) (array stores Fibonacci numbers up to n).
     * - Auxiliary Space: O(n) (array takes extra space).
     * - Time Complexity: O(n) (each value is calculated once).
     *
     * Advantage: Avoids recursion stack overhead.
     */
    public static int fibIterativeDP(int n) {
        if (n <= 1) {
            return n;
        }
        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }

    /**
     * 4. Optimized Iterative Implementation (Constant Space)
     *
     * - Approach: Only keeps track of the last two Fibonacci numbers.
     * - Space Complexity: O(1) (only two variables are used).
     * - Auxiliary Space: O(1) (no extra space grows with n).
     * - Time Complexity: O(n) (each value is calculated once).
     *
     * Advantage: Most memory-efficient implementation.
     */
    public static int fibOptimized(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;

        int a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            int temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }

    /**
     * Main Method to Test All Implementations
     */
    public static void main(String[] args) {
        int n = 10; // Change n for different Fibonacci numbers

        System.out.println("Fibonacci Number at " + n + ":");
        System.out.println("1. Recursive (No Memoization): " + fibRecursive(n));
        System.out.println("2. Recursive (With Memoization): " + fibMemoization(n));
        System.out.println("3. Iterative (Dynamic Programming): " + fibIterativeDP(n));
        System.out.println("4. Optimized Iterative: " + fibOptimized(n));
    }
}
