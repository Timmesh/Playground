# Tuple vs Immutability:

t = (10, 20, 30, 40)

# Trying to change the content of a tuple will result in a TypeError because tuples are immutable.
t[1] = 70  # TypeError: 'tuple' object does not support item assignment
