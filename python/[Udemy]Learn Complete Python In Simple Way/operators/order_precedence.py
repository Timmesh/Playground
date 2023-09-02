# Operator Precedence

# Operator precedence defines the order in which multiple operators are evaluated in an expression.
# Operators with higher precedence are evaluated first, followed by operators with lower precedence.

# Example:
print(3 + 10 * 2)  # 23
print((3 + 10) * 2)  # 26

# In the first example, the multiplication operator (*) has higher precedence than the addition operator (+).
# So, 10 * 2 is evaluated first, resulting in 20, and then 3 + 20 is evaluated, resulting in 23.

# In the second example, the parentheses are used to change the order of evaluation.
# The expression inside the parentheses (3 + 10) is evaluated first, resulting in 13, and then 13 * 2 is evaluated, resulting in 26.

# Let's try more examples:

a, b, c, d = 30, 20, 10, 5
print((a + b) * c / d)  # 100.0
print((a + b) * (c / d))  # 100.0
print(a + (b * c) / d)  # 70.0

# In the first example, (a + b) is evaluated first, resulting in 50.
# Then, 50 * c is evaluated, resulting in 500, and finally, 500 / d is evaluated, resulting in 100.0.

# In the second example, the expression inside the parentheses (a + b) is again evaluated first, resulting in 50.
# Then, c / d is evaluated, resulting in 2.0, and finally, 50 * 2.0 is evaluated, resulting in 100.0.

# In the third example, (b * c) is evaluated first, resulting in 200.
# Then, 200 / d is evaluated, resulting in 40, and finally, a + 40 is evaluated, resulting in 70.0.

# It is important to use parentheses when needed to control the order of evaluation and obtain the correct result.

# Simple Example:
x = 5 + 2 * 3  # Here, the multiplication is evaluated first, so x = 5 + 6 = 11
print(x)  # Output: 11

y = (5 + 2) * 3  # Here, the addition inside parentheses is evaluated first, so y = 7 * 3 = 21
print(y)  # Output: 21
