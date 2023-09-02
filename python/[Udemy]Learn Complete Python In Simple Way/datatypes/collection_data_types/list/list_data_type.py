# Python List Data Type

# Lists are a collection of items that can be of different data types.
# Lists are mutable, meaning we can change their elements after they are created.

# Example 1: Creating a List
my_list = [10, 10.5, 'durga', True, 10]
print(my_list)  # Output: [10, 10.5, 'durga', True, 10]

# Example 2: Accessing Elements in the List
my_list = [10, 20, 30, 40]
print(my_list[0])  # Output: 10 (access first element)
print(my_list[-1])  # Output: 40 (access last element)
print(my_list[1:3])  # Output: [20, 30] (slice from index 1 to 2)

# Example 3: Modifying Elements in the List
my_list[0] = 100  # Change the first element to 100
for item in my_list:
    print(item)  # Output: 100 20 30 40 (loop through the modified list)

# Example 4: Growing the List
my_list = [10, 20, 30]
my_list.append("durga")  # Append "durga" to the end of the list
print(my_list)  # Output: [10, 20, 30, 'durga']

# Example 5: Removing Elements from the List
my_list.remove(20)  # Remove the element with value 20
print(my_list)  # Output: [10, 30, 'durga']

# Example 6: Replicating the List
my_list2 = my_list * 2  # Replicate the list twice
print(my_list2)  # Output: [10, 30, 'durga', 10, 30, 'durga']
