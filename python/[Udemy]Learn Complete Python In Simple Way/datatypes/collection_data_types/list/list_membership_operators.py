# Membership Operators: in and not in

# The in operator checks whether an element exists in the list. If the element is present in the list, it returns True; otherwise, it returns False.
n = [10, 20, 30, 40]

print(10 in n)     # Output: True (Since 10 is present in the list)
print(10 not in n) # Output: False (Since 10 is present in the list, not in returns the opposite)

# If the element is not present in the list, in operator returns False and not in operator returns True.
print(50 in n)     # Output: False (Since 50 is not present in the list)
print(50 not in n) # Output: True (Since 50 is not present in the list, not in returns the opposite)
