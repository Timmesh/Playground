# Set Comprehension:

# Set comprehension is a concise way of creating sets based on some condition or expression.
# The general syntax for set comprehension is {expression for item in iterable if condition}

# Example 1:
s = {x*x for x in range(5)}
print(s)  # {0, 1, 4, 9, 16}

# Explanation:
# In this example, we use set comprehension to create a set 's' that contains the squares of numbers from 0 to 4 (range(5)).
# The expression x*x calculates the square of each number in the range, and the resulting set contains the unique squares.

# Example 2:
s = {2**x for x in range(2, 10, 2)}
print(s)  # {16, 256, 64, 4}

# Explanation:
# Here, we use set comprehension to create a set 's' that contains the powers of 2 with even exponents from 2 to 8 (range(2, 10, 2)).
# The expression 2**x calculates the powers of 2 for each even value of x, and the resulting set contains the unique values.

# Set Objects and Indexing/Slicing:
# Set objects don't support indexing or slicing since they are unordered collections.
# Therefore, attempting to access elements using indexing or slicing will result in a TypeError.
# This is because sets are based on hashing, and their elements are not stored in a specific order that can be accessed by index.
s = {10, 20, 30, 40}
print(s[0])    # TypeError: 'set' object does not support indexing
print(s[1:3])  # TypeError: 'set' object is not subscriptable
