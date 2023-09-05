# Decorator is a function which can take a function as an argument and extend its functionality
# and returns a modified function with extended functionality.

# The main objective of decorator functions is we can extend the functionality of existing
# functions without modifying that function.
def add_decor(func):
    # Define an inner function that extends the functionality of the provided function (func)
    def inner(a, b):
        print('The sum of two numbers is', end=' ')
        # Call the original function (func) with the provided arguments (a, b)
        func(a, b)

    # Return the inner function, effectively replacing the original function with the inner function
    return inner

# Use the @add_decor decorator on the add function
@add_decor
def add(a, b):
    print(a + b)

# Call the decorated add function
add(10, 10)
