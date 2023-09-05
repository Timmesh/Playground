# try with Multiple except Blocks:
# The way of handling exceptions can vary from exception to exception.
# For each specific exception type, we should provide a separate 'except' block.
# This allows us to perform different actions for different types of exceptions.
# If multiple 'except' blocks are available, the one corresponding to the raised exception will be executed.

try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    result = x / y
except ZeroDivisionError:
    # Handling the ZeroDivisionError exception.
    print("Can't Divide by Zero")
except ValueError:
    # Handling the ValueError exception.
    print("Please provide valid integer values")

# Single except Block that can handle Multiple Exceptions:
# We can also use a single 'except' block to handle multiple different types of exceptions.
# These exceptions are specified in parentheses and are treated as a tuple.
# This single 'except' block can catch any of the specified exceptions.

try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    result = x / y
except (ZeroDivisionError, ValueError) as msg:
    # Handling both ZeroDivisionError and ValueError exceptions in a single 'except' block.
    # The 'msg' variable will contain information about the raised exception.
    print("Please provide valid numbers only. The problem is:", msg)
