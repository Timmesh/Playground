# Arithmetic Operators

# Arithmetic operators are used to perform various arithmetic operations in Python.

# Example:
a, b = 10, 2

# Addition
print('a + b =', a + b)  # a + b = 12

# Subtraction
print('a - b =', a - b)  # a - b = 8

# Multiplication
print('a * b =', a * b)  # a * b = 20

# Division
print('a / b =', a / b)  # a / b = 5.0

# Floor Division
print('a // b =', a // b)  # a // b = 5
print('a // b =', 7 // 3)  # 7 // 3 = 2


# Modulo (Remainder)
print('a % b =', a % b)  # a % b = 0
print('a % b =', 7 % 3)  # 7 % 3 = 1

# Exponentiation (Power)
print('a ** b =', a ** b)  # a ** b = 100

# Floating-point and Integral Arithmetic

a, b = 10.5, 2

# Addition
print(a + b)  # 12.5

# Subtraction
print(a - b)  # 8.5

# Multiplication
print(a * b)  # 21.0

# Division
print(a / b)  # 5.25

# Floor Division
print(a // b)  # 5.0

# Modulo (Remainder)
print(a % b)  # 0.5

# Exponentiation (Power)
print(a ** b)  # 110.25

# Note:
# The / operator always performs floating point arithmetic, so the result will be a float.
# The // operator can perform both floating point and integral arithmetic.
# If both arguments are int type, the result will be int type.
# If at least one argument is float type, the result will be float type.

# Division by zero will raise a ZeroDivisionError.
# For any number x, x / 0 and x % 0 will raise a ZeroDivisionError.
# Example:
# 10 / 0  # ZeroDivisionError
# 10.0 / 0  # ZeroDivisionError
