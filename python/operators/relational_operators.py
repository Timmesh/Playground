# Relational Operators: >, >=, <, <=

# Relational operators are used to compare values and return boolean values (True or False) based on the comparison.

# Example:
a, b = 10, 20

# Greater than (>)
print("a > b is", a > b)  # a > b is False

# Greater than or equal to (>=)
print("a >= b is", a >= b)  # a >= b is False

# Less than (<)
print("a < b is", a < b)  # a < b is True

# Less than or equal to (<=)
print("a <= b is", a <= b)  # a <= b is True

# Relational Operators with Strings
a = "Nakul"
b = "Nakul"

# Relational operators can be applied to string types as well.
print("a = b is", a <= b)  # a = b is True
print("a > b is", a > b)  # a > b is False
print("a >= b is", a >= b)  # a >= b is True
print("a < b is", a < b)  # a < b is False
print("a <= b is", a <= b)  # a <= b is True

# Comparison with booleans
print(True > True)  # False
print(True >= True)  # True
print(10 > True)  # True:True is a boolean value with a value of 1 in a numeric context.
print(False > True)  # False

# TypeError: '>' not supported between instances of 'int' and 'str'
# print(10 > 'durga')

# Chaining of Relational Operators
print(10 < 20)  # True
print(10 < 20 < 30)  # True
print(10 < 20 < 30 < 40)  # True
print(10 < 20 < 30 < 40 > 50)  # False
