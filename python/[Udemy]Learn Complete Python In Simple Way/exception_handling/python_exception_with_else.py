# Using else Block with try-except-finally:

try:
    # Risky Code: Code that might raise an exception.
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    result = x / y

except ZeroDivisionError:
    # Handling the ZeroDivisionError exception specifically.
    print("ZeroDivisionError: Can't divide by zero")

else:
    # The else block will be executed if there are no exceptions inside the try block.
    # In this case, it will execute when the division operation (x / y) is successful.
    print("Division Successful. Result =", result)

finally:
    # The finally block will always be executed, whether an exception was raised or not.
    # It's used for cleanup or resource releasing operations.
    print("Finally block executed.")

# Additional note: If an exception occurs, the 'else' block will be skipped, and only 'except' and 'finally' will execute.
