# Assignment Operators:

# We can use the assignment operator to assign a value to a variable. Eg: x = 10
# We can combine the assignment operator with some other operator to form a compound assignment operator.

# Example:
x = 10
x += 10  # Compound assignment: x = x + 10

# The following is the list of all possible compound assignment operators in Python.

# +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=

# Compound assignment example:
x = 10
x += 20  # Equivalent to x = x + 20
print(x)  # 30

# Compound assignment with bitwise AND:
x = 10
x &= 5  # Equivalent to x = x & 5
print(x)  # 0

# Other examples:
x = 5
x **= 3  # Equivalent to x = x ** 3
print(x)  # 125

x = 100
x //= 3  # Equivalent to x = x // 3
print(x)  # 33

# These compound assignment operators perform the specified operation and assign the result back to the variable on the left-hand side.
# They are a shorthand way to write common operations that involve updating the value of a variable.
