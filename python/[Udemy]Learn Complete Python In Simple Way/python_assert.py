# Define a function squareIt that calculates the square of a number.
def squareIt(x):
    return x * x

# Use assert statements to check if the square of specific numbers is as expected.
# If the condition is False, AssertionError is raised with an optional message.
assert squareIt(2) == 4, "The square of 2 should be 4"
assert squareIt(3) == 9, "The square of 3 should be 9"
assert squareIt(4) == 16, "The square of 4 should be 16"

# Print the results of squareIt function for some numbers.
print(squareIt(2))
print(squareIt(3))
print(squareIt(4))
