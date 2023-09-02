# Important Functions of Tuple:

# len(): To return the number of elements present in the tuple.
t = (10, 20, 30, 40)
print(len(t))  # 4

# count(): To return the number of occurrences of a given element in the tuple.
t = (10, 20, 10, 10, 20)
print(t.count(10))  # 3

# index(): Returns the index of the first occurrence of the given element.
# If the specified element is not available, then we will get ValueError.
t = (10, 20, 10, 10, 20)
print(t.index(10))  # 0
try:
    print(t.index(30))  # ValueError: tuple.index(x): x not in tuple
except ValueError as e:
    print(e)

# sorted(): To sort elements based on the default natural sorting order.
t = (40, 10, 30, 20)
t1 = sorted(t)
print(t1)  # [10, 20, 30, 40]
print(t)   # (40, 10, 30, 20)

# We can sort in reverse of the default natural sorting order as follows:
t1 = sorted(t, reverse=True)
print(t1)  # [40, 30, 20, 10]

# min() and max() Functions: These functions return the min and max values according to default natural sorting order.
t = (40, 10, 30, 20)
print(min(t))  # 10
print(max(t))  # 40