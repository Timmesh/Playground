# Equality Operators: ==, !=

# Equality operators are used to compare values for equality and return boolean values (True or False) based on the comparison.

# Example:
print(10 == 20)  # False
print(10 != 20)  # True

# Equality operators can be applied to any type, even for incompatible types.
print(10 == True)  # False
print(False == False)  # True
print("durga" == "durga")  # True
print(10 == "durga")  # False

# Chaining of Equality Operators
# In chaining, if at least one comparison returns False, the result is False. Otherwise, the result is True.
print(10 == 20 == 30 == 40)  # False
print(10 == 10 == 10 == 10)  # True
