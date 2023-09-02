# Mathematical Operations on the Set:

# 1. union():
# x.union(y) or x|y -> We can use this function to return all elements present in both sets.
x = {10, 20, 30, 40}
y = {30, 40, 50, 60}
print(x.union(y)) # {10, 20, 30, 40, 50, 60}
print(x | y)      # {10, 20, 30, 40, 50, 60}

# Explanation:
# The union() function or the | operator returns a new set that contains all the elements present in both x and y, without duplicates.

# 2. intersection():
# x.intersection(y) or x&y -> Returns common elements present in both x and y.
x = {10, 20, 30, 40}
y = {30, 40, 50, 60}
print(x.intersection(y)) # {30, 40}
print(x & y)             # {30, 40}

# Explanation:
# The intersection() function or the & operator returns a new set that contains only the common elements present in both x and y.

# 3. difference():
# x.difference(y) or x-y -> Returns the elements present in x but not in y.
x = {10, 20, 30, 40}
y = {30, 40, 50, 60}
print(x.difference(y)) # {10, 20}
print(x - y)           # {10, 20}
print(y - x)           # {50, 60}

# Explanation:
# The difference() function or the - operator returns a new set that contains the elements present in x but not in y.

# 4. symmetric_difference():
# x.symmetric_difference(y) or x^y -> Returns elements present in either x or y but not in both.
x = {10, 20, 30, 40}
y = {30, 40, 50, 60}
print(x.symmetric_difference(y)) # {10, 50, 20, 60}
print(x ^ y)                     # {10, 50, 20, 60}

# Explanation:
# The symmetric_difference() function or the ^ operator returns a new set that contains the elements present in either x or y but not in both.
