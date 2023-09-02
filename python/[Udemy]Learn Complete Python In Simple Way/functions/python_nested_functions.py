def outer():
    print("Outer function started")

    # Defining the inner function 'inner'
    def inner():
        print("Inner function execution")
        print("Outer function returning inner function")

    # Returning the inner function from the outer function
    return inner

# Getting the returned function 'f1' from 'outer()'
f1 = outer()

# Calling the returned function 'f1'
# f1()