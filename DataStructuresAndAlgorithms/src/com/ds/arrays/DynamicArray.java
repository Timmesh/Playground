package com.ds.arrays;

import java.util.ArrayList;

public class DynamicArray {
    private ArrayList<Integer> list;

    // Constructor to initialize the dynamic array
    public DynamicArray() {
        list = new ArrayList<>();
    }

    // Insert an element at the end
    public void insert(int element) {
        list.add(element);
    }

    // Insert an element at a specific index
    public void insertAt(int index, int element) {
        if (index < 0 || index > list.size()) {
            System.out.println("Insertion not possible.");
            return;
        }
        list.add(index, element);
    }

    // Search for an element
    public int search(int element) {
        return list.indexOf(element); // Returns -1 if not found
    }

    // Update an element at a specific index
    public void update(int index, int element) {
        if (index < 0 || index >= list.size()) {
            System.out.println("Index out of bounds.");
            return;
        }
        list.set(index, element);
    }

    // Delete an element at a specific index
    public void deleteAt(int index) {
        if (index < 0 || index >= list.size()) {
            System.out.println("Index out of bounds.");
            return;
        }
        list.remove(index);
    }

    // Get an element at a specific index
    public int get(int index) {
        if (index < 0 || index >= list.size()) {
            throw new IndexOutOfBoundsException("Index out of range");
        }
        return list.get(index);
    }

    // Display array elements
    public void display() {
        for (Integer element : list) {
            System.out.print(element + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        DynamicArray dArray = new DynamicArray();
        dArray.insert(10);
        dArray.insert(20);
        dArray.insertAt(1, 15);
        dArray.display(); // Output: 10 15 20
        System.out.println("Search 15: " + dArray.search(15));
        dArray.update(1, 25);
        dArray.display(); // Output: 10 25 20
        dArray.deleteAt(1);
        dArray.display(); // Output: 10 20
    }

    /*
     * Time Complexity:
     * - insert(element): O(1) (amortized) - Inserting at the end.
     * - insertAt(index, element): O(n) - Shifting elements.
     * - search(element): O(n) - Linear search.
     * - update(index, element): O(1) - Direct update via index.
     * - deleteAt(index): O(n) - Shifting elements.
     * - get(index): O(1) - Direct access.
     *
     * Space Complexity:
     * - O(n) - Space for storing 'n' elements in ArrayList.
     *
     * Auxiliary Space:
     * - O(1) - No extra space apart from the ArrayList itself.
     */
}
