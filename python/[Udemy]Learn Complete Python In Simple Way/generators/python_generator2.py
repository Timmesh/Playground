# Generator Functions
# A generator is a function that generates a sequence of values.

# Define a generator function called mygen
def mygen():
    yield 'A'  # Use the 'yield' keyword to return the value 'A'
    yield 'B'  # Use 'yield' to return 'B'
    yield 'C'  # Use 'yield' to return 'C'

# Create a generator object by calling mygen()
g = mygen()

# Check the type of the generator object
print(type(g))  # Output: <class 'generator'>

# Use the 'next()' function to retrieve values from the generator
print(next(g))  # Output: 'A'
print(next(g))  # Output: 'B'
print(next(g))  # Output: 'C'

# If we try to get the next value beyond what the generator yields, it will raise a StopIteration error
# print(next(g))  # Uncommenting this line would result in a StopIteration error
