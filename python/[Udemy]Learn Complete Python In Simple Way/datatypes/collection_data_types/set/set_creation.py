# Creation of Set Objects:

# We can create set objects directly using curly braces {}.
s = {10, 20, 30, 40}
print(s)  # {40, 10, 20, 30}
print(type(s))  # <class 'set'>

# Explanation:
# We created a set s with elements 10, 20, 30, and 40.
# When we print the set, the elements are displayed in an unordered manner, as sets do not preserve insertion order.

# We can also create set objects by using the set() function with any sequence as an argument.

l = [10, 20, 30, 40, 10, 20, 10]
s = set(l)
print(s)  # {40, 10, 20, 30}

# Explanation:
# We have a list l with duplicate elements.
# Using the set() function, we created a set s from the list l, which automatically removes duplicates.

# Another example using range() function to create a set.

s = set(range(5))
print(s)  # {0, 1, 2, 3, 4}

# Explanation:
# We used the range() function to generate numbers from 0 to 4, and then created a set s from those numbers.

# Special care should be taken when creating an empty set. We should use set() function for an empty set.

# Incorrect way of creating an empty set:
s = {}
print(s)  # {}
print(type(s))  # <class 'dict'>

# Explanation:
# If we use curly braces {} to create an empty set, Python will treat it as a dictionary, not an empty set.

# Correct way of creating an empty set:
s = set()
print(s)  # set()
print(type(s))  # <class 'set'>

# Explanation:
# By using set() function without any arguments, we create an empty set. The output will show "set()" to indicate an empty set.
