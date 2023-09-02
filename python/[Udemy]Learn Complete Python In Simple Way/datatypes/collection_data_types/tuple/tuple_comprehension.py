# Tuple Comprehension:

# Tuple comprehension is not supported in Python. It will result in a generator object instead of a tuple.

# Incorrect Tuple Comprehension:
t = (x**2 for x in range(1, 6))
print(type(t))  # <class 'generator'>


# The above expression creates a generator object, not a tuple.

# To get the elements from the generator, we can use a for loop:
for x in t:
    print(x)  # 1 4 9 16 25

# Explanation:
# Tuple comprehension is not directly supported in Python. When we use tuple comprehension syntax,
# it creates a generator expression, which is a type of lazy iterable that produces values on-the-fly when iterated over.
# The generator is not a concrete tuple with all elements at once; rather, it produces elements as needed during iteration.
# Since tuple comprehension is not directly supported, if you need a tuple, you can create it using the tuple() constructor.

# Correct Way:
t = tuple(x**2 for x in range(1, 6))
print(type(t))  # <class 'tuple'>
print(t)  # (1, 4, 9, 16, 25)

# Now, we get a proper tuple by using the tuple() constructor on the generator expression.
