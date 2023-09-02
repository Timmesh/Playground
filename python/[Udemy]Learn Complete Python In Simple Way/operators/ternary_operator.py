# Ternary Operator OR Conditional Operator

# Syntax: x = firstValue if condition else secondValue

# If the condition is True, then the first value will be assigned to 'x', else the second value will be assigned.

# Example:
a, b = 10, 20
x = 30 if a < b else 40
print(x)  # 30

# Read two numbers from the keyboard and print the minimum value
a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
min_value = a if a < b else b
print("Minimum Value:", min_value)

# In this example, we use the ternary operator to determine the minimum value between 'a' and 'b'.
# If 'a' is less than 'b', then 'a' is assigned to 'min_value', otherwise 'b' is assigned.
