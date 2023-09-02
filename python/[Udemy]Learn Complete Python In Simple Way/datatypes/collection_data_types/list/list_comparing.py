# Comparing List Objects:

# When using the equality operator (==), it compares each element of the lists for equality. If all elements in both lists are the same, it returns True, otherwise, it returns False.
x = ["Dog", "Cat", "Rat"]
y = ["Dog", "Cat", "Rat"]
z = ["DOG", "CAT", "RAT"]

print(x == y)  # Output: True
print(x == z)  # Output: False
print(x != z)  # Output: True

# When using relational operators (<, <=, >, >=) between List Objects, only the comparison of the first element will be performed.
x = [50, 20, 30]
y = [40, 50, 60, 100, 200]

print(x > y)  # Output: True (Since the first element in x is greater than the first element in y)
print(x >= y)  # Output: True (Same as above, and also len(x) >= len(y))
print(x < y)  # Output: False (Since the first element in x is not less than the first element in y)
print(x <= y)  # Output: False (Same as above, and also len(x) <= len(y))

# For the relational operators between lists of strings, it performs a lexicographic (dictionary) comparison based on the ASCII values of characters.
x = ["Dog", "Cat", "Rat"]
y = ["Rat", "Cat", "Dog"]

print(x > y)  # Output: False (Since the first element "Dog" in x is not greater than "Rat" in y)
print(x >= y)  # Output: False (Same as above, and also len(x) >= len(y))
print(x < y)  # Output: True (Since the first element "Dog" in x is less than "Rat" in y)
print(x <= y)  # Output: True (Same as above, and also len(x) <= len(y))
