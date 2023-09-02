# Tuple Packing and Unpacking:

# Tuple Packing: Creating a tuple by packing a group of variables.
a, b, c, d = 10, 20, 30, 40
t = a, b, c, d
print(t)  # (10, 20, 30, 40)

# Tuple Unpacking: Unpacking a tuple and assigning its values to different variables.
t = (10, 20, 30, 40)
a, b, c, d = t
print("a=", a, "b=", b, "c=", c, "d=", d)  # a= 10 b= 20 c= 30 d= 40

# Note: At the time of tuple unpacking, the number of variables and number of values should be the same,
# otherwise, we will get ValueError.
t = (10, 20, 30, 40)
try:
    a, b, c = t  # ValueError: too many values to unpack (expected 3)
except ValueError as e:
    print(e)
