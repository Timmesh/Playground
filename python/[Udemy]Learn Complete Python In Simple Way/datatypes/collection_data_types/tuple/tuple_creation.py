# 1. Creation of Empty Tuple

t = ()
print(t)    # Output: ()

# 2. Creation of Single-Valued Tuple, Parentheses are Optional, should end with a Comma

t1 = (10,)
t2 = 10,
print(t1)   # Output: (10,)
print(t2)   # Output: (10,)

# 3. Creation of Multi-Valued Tuples, Parentheses are Optional

t1 = 10, 20, 30
t2 = (10, 20, 30)
print(t1)   # Output: (10, 20, 30)
print(t2)   # Output: (10, 20, 30)

# 4. Using tuple() Function

# We can convert a list or any iterable to a tuple using the tuple() function.
list1 = [10, 20, 30]
t1 = tuple(list1)
print(t1)   # Output: (10, 20, 30)

# We can also convert a range object to a tuple using the tuple() function.
t2 = tuple(range(10, 20, 2))
print(t2)   # Output: (10, 12, 14, 16, 18)
