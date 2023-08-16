# Logical Operators: and, or, not

# Logical operators are used to perform logical operations on boolean values (True or False) and return boolean results.

# For boolean types:
# and: If both arguments are True, then the result is True; otherwise, the result is False.
# or: If at least one argument is True, then the result is True; otherwise, the result is False.
# not: It negates the value. If the value is True, it returns False, and vice versa.

# Example for boolean types:
print(True and False)  # False
print(True or False)  # True
print(not False)  # True

# For non-boolean types:
# 0 means False
# non-zero means True
# empty string is always treated as False

# x and y:
# If x evaluates to False, it returns x; otherwise, it returns y.
print(10 and 20)  # 20 (both are True, so it returns y)
print(0 and 20)  # 0 (x is False, so it returns x)

# x or y:
# If x evaluates to True, it returns x; otherwise, it returns y.
print(10 or 20)  # 10 (x is True, so it returns x)
print(0 or 20)  # 20 (both are False, so it returns y)

# not x:
# If x is False, it returns True; otherwise, it returns False.
print(not 10)  # False (10 is True, so it returns False)
print(not 0)  # True (0 is False, so it returns True)

# Example for non-boolean types:
print("Nakul" and "Timmesh")  # "Timmesh" (both are non-empty strings, so it returns y)
print("" and "Timmesh")  # "" (x is an empty string, so it returns x)
print("Nakul" and "")  # "" (y is an empty string, so it returns y)
print("" or "Timmesh")  # "Timmesh" (both are non-empty strings, so it returns x)
print("Nakul" or "")  # "Nakul" (x is a non-empty string, so it returns x)
print(not "")  # True (x is an empty string, so it returns True)
print(not "Nakul")  # False (x is a non-empty string, so it returns False)
