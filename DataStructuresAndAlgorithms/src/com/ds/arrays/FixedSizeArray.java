package com.ds.arrays;

public class FixedSizeArray {
    private int[] arr;
    private int size;

    // Constructor to initialize the array with a fixed size
    public FixedSizeArray(int capacity) {
        arr = new int[capacity]; // Create the array with a fixed size
        size = 0; // Initialize size to 0
    }

    // Insert an element at a specific index (shift elements if necessary)
    public void insertAt(int index, int element) {
        if (index < 0 || index > size || size >= arr.length) {
            System.out.println("Insertion not possible");
            return;
        }

        // Shift elements to the right to make space
        for (int i = size; i > index; i--) {
            arr[i] = arr[i - 1];
        }

        arr[index] = element; // Insert the new element
        size++; // Increment the size
    }

    // Access an element at a specific index
    public int get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of range");
        }
        return arr[index];
    }

    // Display the array elements
    public void display() {
        for (int i = 0; i < size; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        FixedSizeArray fsArray = new FixedSizeArray(5); // Fixed size array of capacity 5
        fsArray.insertAt(0, 10);
        fsArray.insertAt(1, 20);
        fsArray.insertAt(2, 30);
        fsArray.insertAt(1, 25); // Insert at position 1
        fsArray.display(); // Output: 10 25 20 30
    }

    /*
     * Time Complexity:
     * - insertAt(index, element): O(n) - Inserting an element in the middle/beginning requires shifting elements.
     * - get(index): O(1) - Direct access to array elements.
     * - display(): O(n) - Iterates over the array to print all elements.
     *
     * Space Complexity:
     * - O(n) - Fixed-size array uses a contiguous block of memory to store elements.
     *
     * Auxiliary Space:
     * - O(1) - The algorithm does not use extra space proportional to input size, except for the input itself.
     */
}