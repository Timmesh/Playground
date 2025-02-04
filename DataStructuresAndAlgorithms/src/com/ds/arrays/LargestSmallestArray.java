package com.ds.arrays;

/**
 * Class to find the largest and smallest elements in an array.
 *
 * Time Complexity:
 * - Finding the largest or smallest element: O(n)
 *
 * Space Complexity:
 * - O(1) for both largest and smallest element finding methods.
 *
 * Auxiliary Space:
 * - O(1) as only a constant amount of extra space is used.
 */
public class LargestSmallestArray {

    /**
     * Finds the largest element in the array.
     *
     * @param arr The input array
     * @return The largest element in the array
     */
    public static int findLargest(int[] arr) {
        // Edge case: if array is empty, return Integer.MIN_VALUE
        if (arr.length == 0) {
            throw new IllegalArgumentException("Array cannot be empty");
        }

        int largest = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > largest) {
                largest = arr[i];
            }
        }
        return largest;
    }

    /**
     * Finds the smallest element in the array.
     *
     * @param arr The input array
     * @return The smallest element in the array
     */
    public static int findSmallest(int[] arr) {
        // Edge case: if array is empty, return Integer.MAX_VALUE
        if (arr.length == 0) {
            throw new IllegalArgumentException("Array cannot be empty");
        }

        int smallest = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < smallest) {
                smallest = arr[i];
            }
        }
        return smallest;
    }

    public static void main(String[] args) {
        int[] arr = {3, 5, 7, 2, 8, -1, 4};

        // Test the methods
        System.out.println("Largest element: " + findLargest(arr)); // Output: 8
        System.out.println("Smallest element: " + findSmallest(arr)); // Output: -1
    }
}