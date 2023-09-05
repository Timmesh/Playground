# How to Print Exception Information:
try:
    result = 10 / 0  # Attempting to divide by zero, which raises a ZeroDivisionError
except ZeroDivisionError as msg:
    # When an exception occurs, we can catch it using the 'except' block and assign it to a variable, here 'msg'.
    # Then, we can print the description or information about the exception.
    print("Exception raised and its description is:", msg)
