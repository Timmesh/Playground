# Python Immutability and Object Identity Examples

# All fundamental data types in Python are immutable, meaning once an object is created, its value cannot be changed.
# If we try to change the value, a new object will be created with the updated value.

# Example 1: Integers
a = 10
b = 10
print(a is b)  # Output: True (both a and b refer to the same object)
print(id(a))  # Output: 1572353952 (memory address of the object)
print(id(b))  # Output: 1572353952 (memory address of the same object)

a = a + 1  # a is now reassigned to a new object with value 11
print(id(a))  # Output: Different memory address for the new object

# Example 2: Complex Numbers
a = 10 + 5j
b = 10 + 5j
print(a is b)  # Output: False (a and b refer to different objects)
print(id(a))  # Output: Different memory address for object a
print(id(b))  # Output: Different memory address for object b

# Example 3: Booleans
a = True
b = True
print(a is b)  # Output: True (both a and b refer to the same object)
print(id(a))  # Output: 1572172624 (memory address of the object)
print(id(b))  # Output: 1572172624 (memory address of the same object)

# Example 4: Strings
a = 'durga'
b = 'durga'
print(a is b)  # Output: True (both a and b refer to the same object)
print(id(a))  # Output: 16378848 (memory address of the object)
print(id(b))  # Output: 16378848 (memory address of the same object)

# The id function returns the memory address of the object.
