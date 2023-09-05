# Default except Block:
# We can use a default 'except' block to handle any type of exceptions.
# In the default 'except' block, we can provide generic error messages or actions
# to be taken for any exception not handled specifically.

try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    result = x / y
except ZeroDivisionError:
    # Handling the ZeroDivisionError exception specifically.
    print("ZeroDivisionError: Can't divide by zero")
except BaseException as e:
    # Default 'except' block to handle any other exceptions.
    # This block will be executed if the exception is not ZeroDivisionError.
    print("Default Except: Please provide valid input only",e)
