# How to Define and Raise Customized Exceptions:

# Every exception in Python is a class that extends the Exception class, either directly
# or indirectly.

# Syntax for creating a customized exception class:
# class CustomExceptionClassName(Exception):
#     def __init__(self, arg):
#         self.msg = arg

# We can raise a customized exception using the 'raise' keyword as follows:
# raise CustomExceptionClassName("message")

# Example 1: Creating a customized exception class TooYoungException
class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg = arg

# Example 2: Creating another customized exception class TooOldException
class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg

# Taking user input for age
age = int(input("Enter Age:"))

# Checking age and raising custom exceptions accordingly
if age > 60:
    raise TooOldException("Your age has already crossed the marriage age...no chance of getting married")
elif age < 18:
    raise TooYoungException("Please wait some more time; you will get the best match soon!!!")

else:
    print("You will get match details soon by email!!!")
