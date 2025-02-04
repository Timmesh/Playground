package com.ds.arrays;

/**
 * Class to find the second largest and second smallest elements in an array.
 *
 * Time Complexity:
 * - Finding the second largest or second smallest element: O(n)
 *
 * Space Complexity:
 * - O(1) for both methods.
 *
 * Auxiliary Space:
 * - O(1) as only a constant amount of extra space is used.
 */
public class SecondLargestSmallestArray {

    /**
     * Finds the second largest element in the array.
     *
     * @param arr The input array
     * @return The second largest element in the array
     * @throws IllegalArgumentException if the array has fewer than two distinct elements
     */
    public static int findSecondLargest(int[] arr) {
        if (arr.length < 2) {
            throw new IllegalArgumentException("Array must have at least two elements");
        }

        int largest = Integer.MIN_VALUE;
        int secondLargest = Integer.MIN_VALUE;
        boolean distinctFound = false;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > largest) {
                secondLargest = largest;
                largest = arr[i];
                distinctFound = true;
            } else if (arr[i] > secondLargest && arr[i] != largest) {
                secondLargest = arr[i];
                distinctFound = true;
            }
        }

        if (!distinctFound) {
            throw new IllegalArgumentException("Array has fewer than two distinct elements");
        }

        return secondLargest;
    }

    /**
     * Finds the second smallest element in the array.
     *
     * @param arr The input array
     * @return The second smallest element in the array
     * @throws IllegalArgumentException if the array has fewer than two distinct elements
     */
    public static int findSecondSmallest(int[] arr) {
        if (arr.length < 2) {
            throw new IllegalArgumentException("Array must have at least two elements");
        }

        int smallest = Integer.MAX_VALUE;
        int secondSmallest = Integer.MAX_VALUE;
        boolean distinctFound = false;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < smallest) {
                secondSmallest = smallest;
                smallest = arr[i];
                distinctFound = true;
            } else if (arr[i] < secondSmallest && arr[i] != smallest) {
                secondSmallest = arr[i];
                distinctFound = true;
            }
        }

        if (!distinctFound) {
            throw new IllegalArgumentException("Array has fewer than two distinct elements");
        }

        return secondSmallest;
    }

    public static void main(String[] args) {
        int[] arr = {3, 5, 7, 2, 8, -1, 4};

        System.out.println("Second Largest element: " + findSecondLargest(arr)); // Output: 7
        System.out.println("Second Smallest element: " + findSecondSmallest(arr)); // Output: 2

        // Example where largest number is repeating
        int[] arrSame = {3, 3, 3, 3, 5};
        try {
            System.out.println("Second Largest element (largest repeating): " + findSecondLargest(arrSame)); // Output: 3
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage()); // Output: Array has fewer than two distinct elements
        }

        try {
            System.out.println("Second Smallest element (largest repeating): " + findSecondSmallest(arrSame)); // Output: 3
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage()); // Output: Array has fewer than two distinct elements
        }
    }
}
