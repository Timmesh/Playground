# Java Array Implementations

---

## 1. FixedSizeArray.java
- **Implementation of a Static (Fixed-Size) Array.**
- CRUD operations: `insert`, `insertAt`, `search`, `update`, `deleteAt`, `get`, `display`.
- Inline comments for **Time Complexity**, **Space Complexity**, and **Auxiliary Space**.

---

## 2. DynamicArray.java
- **Implementation of a Dźynamic Array (`ArrayList`).**
- CRUD operations: `insert`, `insertAt`, `search`, `update`, `deleteAt`, `get`, `display`.
- Inline comments for **Time Complexity**, **Space Complexity**, and **Auxiliary Space**.

---

## 3. LargestSmallestArray.java
- **Implementation to find the largest and smallest element in an array.**
- Operations:
	- `findLargest`: Finds the largest element in the array.
	- `findSmallest`: Finds the smallest element in the array.
- **Time Complexity**:
	- `findLargest`: O(n)
	- `findSmallest`: O(n)
- **Space Complexity**:
	- Both methods use **O(1)** space.
- **Auxiliary Space**:
	- Both methods use **O(1)** auxiliary space as only a constant amount of extra space is used.

## 4. SecondLargestSmallestArray.java
- **Implementation to find the second largest and second smallest elements in an array.**
- Operations:
	- `findSecondLargest`: Finds the second largest element in the array. Handles cases where the largest element is repeated.
	- `findSecondSmallest`: Finds the second smallest element in the array. Handles cases where the smallest element is repeated.
- **Time Complexity**:
	- `findSecondLargest`, `findSecondSmallest`: O(n)
- **Space Complexity**:
	- Both methods use **O(1)** space.
- **Auxiliary Space**:
	- Both methods use **O(1)** auxiliary space as only a constant amount of extra space is used.
- **Boundary Condition**:
	- If all elements are the same or if there are fewer than two distinct elements, an exception is thrown stating "Array has fewer than two distinct elements".