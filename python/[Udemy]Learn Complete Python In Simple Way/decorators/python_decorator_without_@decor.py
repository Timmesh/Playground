# Define a decorator function without using the @decorator syntax
def add_decor(func):
    # Define an inner function that extends the functionality of the provided function (func)
    def inner(a, b):
        if a == 0 or b == 0:
            # If either a or b is zero, call the original function directly
            func(a, b)
        else:
            # If both a and b are non-zero, print the sum of the two numbers
            print('The sum of two numbers is', end=' ')
            # Call the original function (func) with the provided arguments (a, b)
            func(a, b)

    # Return the inner function, effectively replacing the original function with the inner function
    return inner

# Define the add function
def add(a, b):
    print(a + b)

# Create a decorated version of the add function
f1 = add_decor(add)

# Call the decorated add function with different arguments
f1(10, 20)  # Output: The sum of two numbers is 30
f1(10, 0)   # Output: 10 (original add function called directly because one of the arguments is 0)
