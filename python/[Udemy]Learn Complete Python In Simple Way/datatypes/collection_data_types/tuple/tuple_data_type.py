# Tuple Data Type

# A tuple is similar to a list, but it is immutable. Once a tuple is created, we cannot modify its elements.
# Tuple supports both positive and negative indexing. Positive index represents forward direction (left to right) and negative index represents backward direction (right to left).

t = (10, 20, 30, 40)
type(t)    # Output: <class 'tuple'>

# Since tuples are immutable, we cannot modify its elements, and attempting to do so will result in an error.
# Uncomment the lines below to see the TypeError and AttributeError that will be raised.
# t[0] = 100  # TypeError: 'tuple' object does not support item assignment
# t.append("durga")   # AttributeError: 'tuple' object has no attribute 'append'
# t.remove(10)    # AttributeError: 'tuple' object has no attribute 'remove'

# Parentheses are optional but recommended to use when defining a tuple.
t = 10, 20, 30, 40
print(t)    # Output: (10, 20, 30, 40)

# An empty tuple can be created using parentheses.
t = ()
print(type(t))    # Output: <class 'tuple'>

# Special care must be taken when creating a single-valued tuple. The value should end with a comma to be considered a tuple.
t = (10)
print(t)    # Output: 10
print(type(t))    # Output: <class 'int'>

t = (10,)
print(t)    # Output: (10,)
print(type(t))    # Output: <class 'tuple'>
