# finally Block:
# The main purpose of the finally block is to maintain clean-up code.
# It is executed always, whether an exception is raised or not, and whether an exception is handled or not.
# It is recommended to use the finally block to release resources and perform clean-up tasks.

try:
    # Risky Code
    print("try")
except:
    # Handling Code (This block won't be executed if no exception is raised)
    print("except")
finally:
    # Clean-up code (This block will be executed always)
    print("finally")

# Case-1: If there is no exception
try:
    print("try")
except:
    print("except")
finally:
    print("finally")
# Output:
# try
# finally

# Case-2: If there is an exception raised but handled
try:
    print("try")
    print(10 / 0)
except ZeroDivisionError:
    print("except")
finally:
    print("finally")
# Output:
# try
# except
# finally

# Case-3: If there is an exception raised but not handled
try:
    print("try")
    print(10 / 0)
except NameError:
    print("except")
finally:
    print("finally")
# Output:
# try
# finally
# ZeroDivisionError: division by zero (Abnormal Termination)

# Note: The finally block won't be executed if os._exit(0) function is used.
# Whenever os._exit(0) is called, Python Virtual Machine itself will be shut down.
import os

try:
    print("try")
    os._exit(0)
except NameError:
    print("except")
finally:
    print("finally")
# Output: try (No finally execution)
