# What is Exception?
# An unwanted and unexpected event that disturbs the normal flow of a program is called an exception.
# Examples of exceptions include ZeroDivisionError, TypeError, ValueError, FileNotFoundError, EOFError, and more.

# Example 1: ZeroDivisionError
try:
    result = 10 / 0  # Division by zero will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Exception: Division by zero")

# Example 2: TypeError
try:
    result = 10 / "two"  # TypeError: unsupported operand type(s) for /: 'int' and 'str'
except TypeError as e:
    print(f"Exception: {e}")

# Example 3: ValueError
try:
    number = int("ten")  # ValueError: invalid literal for int() with base 10: 'ten'
except ValueError as e:
    print(f"Exception: {e}")

# Exception handling is crucial to ensure graceful termination of the program.
# It allows us to define alternative ways to continue the program, even when exceptions occur.

# Example 4: FileNotFoundError
try:
    # Read data from a remote file located in London (simulated)
    remote_file = open("LondonData.txt", "r")
except FileNotFoundError:
    # If the London file is not available, use a local file and continue normally.
    local_file = open("LocalData.txt", "r")
    data = local_file.read()
    local_file.close()
    print("Using local data:", data)
