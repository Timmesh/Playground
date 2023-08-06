# To get Information about List:

# len(): Returns the number of elements present in the list
n = [10, 20, 30, 40]
print(len(n))  # Output: 4 (number of elements in the list)

# count(): Returns the number of occurrences of the specified item in the list
n = [1, 2, 2, 2, 2, 3, 3]
print(n.count(1))  # Output: 1 (number of occurrences of 1 in the list)
print(n.count(2))  # Output: 4 (number of occurrences of 2 in the list)
print(n.count(3))  # Output: 2 (number of occurrences of 3 in the list)
print(n.count(4))  # Output: 0 (number of occurrences of 4 in the list)

# index(): Returns the index of the first occurrence of the specified item.
n = [1, 2, 2, 2, 2, 3, 3]
print(n.index(1))  # Output: 0 (index of the first occurrence of 1 in the list)
print(n.index(2))  # Output: 1 (index of the first occurrence of 2 in the list)
print(n.index(3))  # Output: 5 (index of the first occurrence of 3 in the list)
#print(n.index(4)) # ValueError: 4 is not in list

# If the specified element is not present in the list, then we will get ValueError.
# Hence, before using the index() method, we have to check whether the item is present in the list or not using the in operator.
print(4 in n)  # Output: False (4 is not present in the list)

# clear() Function

# The clear() function is used to remove all elements from the list, making it empty.

n = [10, 20, 30, 40]
print(n)     # Output: [10, 20, 30, 40]

n.clear()
print(n)     # Output: [] (The list is now empty after calling the clear() function)
