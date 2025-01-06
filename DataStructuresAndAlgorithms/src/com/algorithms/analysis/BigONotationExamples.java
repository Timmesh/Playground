package com.algorithms.analysis;

public class BigONotationExamples {

    /**
     * 1. Simple For Loop (O(n))
     * - Time Complexity: O(n)
     * - Explanation: The loop runs 'n' times, and each iteration takes O(1) time.
     */
    public static void simpleLoop(int n) {
        System.out.println("\n1. Simple Loop (O(n))");
        for (int i = 0; i < n; i++) {
            System.out.print(i + " ");
        }
    }

    /**
     * 2. Nested For Loop (O(n^2))
     * - Time Complexity: O(n^2)
     * - Explanation: The outer loop runs 'n' times, and for each outer loop,
     *   the inner loop runs 'n' times. Total iterations = n * n.
     */
    public static void nestedLoop(int n) {
        System.out.println("\n\n2. Nested Loop (O(n^2))");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print("(" + i + "," + j + ") ");
            }
        }
    }

    /**
     * 3. Sequential Loops (O(n + m))
     * - Time Complexity: O(n + m)
     * - Explanation: Two independent loops. Their time complexities add up.
     */
    public static void sequentialLoops(int n, int m) {
        System.out.println("\n\n3. Sequential Loops (O(n + m))");

        for (int i = 0; i < n; i++) {
            System.out.print(i + " ");
        }

        for (int j = 0; j < m; j++) {
            System.out.print(j + " ");
        }
    }

    /**
     * 4. Logarithmic Loop (O(log n))
     * - Time Complexity: O(log n)
     * - Explanation: The loop variable doubles each iteration. Runs approx log₂(n) times.
     */
    public static void logarithmicLoop(int n) {
        System.out.println("\n\n4. Logarithmic Loop (O(log n))");
        for (int i = 1; i < n; i *= 2) {
            System.out.print(i + " ");
        }
    }

    /**
     * 5. Nested Logarithmic Loop (O(n log n))
     * - Time Complexity: O(n log n)
     * - Explanation: Outer loop runs 'n' times, and the inner loop runs 'log₂(n)' times.
     */
    public static void nestedLogarithmicLoop(int n) {
        System.out.println("\n\n5. Nested Logarithmic Loop (O(n log n))");
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < n; j *= 2) {
                System.out.print("(" + i + "," + j + ") ");
            }
        }
    }

    /**
     * 6. While Loop (O(n))
     * - Time Complexity: O(n)
     * - Explanation: The loop executes 'n' times before the condition becomes false.
     */
    public static void whileLoop(int n) {
        System.out.println("\n\n6. While Loop (O(n))");
        int i = 0;
        while (i < n) {
            System.out.print(i + " ");
            i++;
        }
    }

    /**
     * 7. Exponential Loop (O(2^n))
     * - Time Complexity: O(2^n)
     * - Explanation: Each recursive call creates two additional calls.
     */
    public static int exponentialLoop(int n) {
        if (n == 0) return 1;
        if (n == 1) return 1;
        return exponentialLoop(n - 1) + exponentialLoop(n - 1);
    }

    /**
     * 8. Factorial Loop (O(n!))
     * - Time Complexity: O(n!)
     * - Explanation: Each level of recursion spawns 'n' recursive calls.
     */
    public static void factorialLoop(int n) {
        if (n == 0) return;
        for (int i = 0; i < n; i++) {
            factorialLoop(n - 1);
        }
    }

    /**
     * Main Method
     */
    public static void main(String[] args) {
        int n = 5;
        int m = 3;

        System.out.println("=== Big O Notation Examples ===");
        simpleLoop(n);              // O(n)
        nestedLoop(n);              // O(n^2)
        sequentialLoops(n, m);      // O(n + m)
        logarithmicLoop(n);         // O(log n)
        nestedLogarithmicLoop(n);   // O(n log n)
        whileLoop(n);               // O(n)

        System.out.println("\n\n7. Exponential Loop (O(2^n))");
        System.out.println("Exponential result for n=" + n + ": " + exponentialLoop(n));

        System.out.println("\n8. Factorial Loop (O(n!)) - Avoid running for large n, can cause stack overflow!");
    }
}
