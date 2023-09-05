# Types of Exceptions in Python:

# 1) Predefined Exceptions:
# - Also known as inbuilt exceptions.
# - These exceptions are raised automatically by the Python virtual machine when
#   a particular event occurs.
# - For example, trying to perform Division by zero will automatically raise
#   the ZeroDivisionError.
#   print(10/0)
# - Another example is trying to convert an input value to an int type, and if the
#   input value is not an int, Python will raise a ValueError automatically.
#   x = int("ten")  # ValueError

# 2) User Defined Exceptions:
# - Also known as Customized Exceptions or Programmatic Exceptions.
# - Sometimes, we need to define and raise exceptions explicitly to indicate that
#   something has gone wrong. Such exceptions are called User Defined Exceptions.
# - Python doesn't have any built-in knowledge of these exceptions; programmers
#   are responsible for defining and raising them explicitly using the "raise" keyword.

try:
    print("try")
    try:
        print("inner try")
    except:
        print("except")
except:
    print("except")
finally:
    print("finally")

# In this example, we have nested try-except blocks. If an exception occurs in the inner
# try block, it will be caught by the inner except block, and the "except" block inside
# the outer try block will not execute. Finally, the "finally" block will execute
# regardless of whether an exception was raised or not.
