# Accessing Elements of List

# By using Index:
# Lists follow zero-based indexing, where the index of the first element is zero.

my_list = [10, 20, 30, 40]
print(my_list[0])  # Output: 10 (access the first element)
print(my_list[-1])  # Output: 40 (access the last element)
#print(my_list[10])  # Output: IndexError: list index out of range (index is out of bounds)

# By using Slice Operator:
# Syntax: list2 = list1[start:stop:step]

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[2:7:2])  # Output: [3, 5, 7] (slice from index 2 to 6 with a step of 2)
print(n[4::2])  # Output: [5, 7, 9] (slice from index 4 to the end with a step of 2)
print(n[3:7])  # Output: [4, 5, 6, 7] (slice from index 3 to 6)
print(n[8:2:-2])  # Output: [9, 7, 5] (slice in reverse order with a step of -2)
print(n[4:100])  # Output: [5, 6, 7, 8, 9, 10] (slice from index 4 to the end)
