# Special Operators: Identity Operators, Membership Operators

# Identity Operators: is, is not
# These operators are used for address comparison.
# 'is' returns True if both variables point to the same object.
# 'is not' returns True if both variables do not point to the same object.

# Example:
a, b = 10, 10
print(a is b)  # True

x = True
y = True
print(x is y)  # True

# The 'is' operator is useful to check if two variables are referring to the same object in memory.
# In the first example, a and b both have the value 10, and Python creates a single memory object for small integers.
# Hence, a and b refer to the same memory location, so 'a is b' returns True.

# However, for larger integers or objects, Python creates separate memory locations for each variable.
# In such cases, 'is' will return False even if the values are equal.
# Example:
a = 1000
b = 1000
print(a is b)  # False

# Membership Operators: in, not in
# These operators are used to check if a given object is present in a specified collection.
# 'in' returns True if the object is present, 'not in' returns True if the object is not present.

# Example:
x = "hello learning Python is very easy!!!"
print('h' in x)  # True
print('d' in x)  # False
print('d' not in x)  # True
print('Python' in x)  # True

list1 = ["sunny", "bunny", "chinny", "pinny"]
print("sunny" in list1)  # True
print("snny" in list1)  # False
print("snny" not in list1)  # True

# These operators are helpful when working with collections like strings, lists, sets, tuples, and dictionaries.
# 'in' checks if an element is present in the collection, and 'not in' checks if an element is absent.
