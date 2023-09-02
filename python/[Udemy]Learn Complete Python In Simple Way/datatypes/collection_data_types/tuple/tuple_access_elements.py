# Accessing Elements of Tuple:

# 1. By using Index:

t = (10, 20, 30, 40, 50, 60)
print(t[0])     # Output: 10
print(t[-1])    # Output: 60

# Trying to access an index that is out of range will result in an IndexError.
#print(t[100])   # IndexError: tuple index out of range

# 2. By using Slice Operator:

t = (10, 20, 30, 40, 50, 60)
# Slice operator extracts the elements from index 2 to 4 (5-1).
print(t[2:5])   # Output: (30, 40, 50)

# Even if the stop index is out of range, it will be ignored and all elements up to the end of the tuple will be returned.
print(t[2:100]) # Output: (30, 40, 50, 60)

# Slice operator with a step of 2 extracts elements with a step of 2.
print(t[::2])   # Output: (10, 30, 50)
