# EXCEPTION HANDLING

# In any programming language, there are 2 types of errors possible: Syntax Errors and Runtime Errors.

# Syntax Errors:
# These errors occur due to invalid syntax in the code.
# Programmer is responsible to correct these syntax errors.
# Once all syntax errors are corrected, program execution will start.

# Example of Syntax Error:
# Incomplete code block (missing ':')

#x = 10
#if x == 10  # SyntaxError: invalid syntax Missing :
#    print("Hello")

# Missing parentheses in the print statement
#print
#"Hello"  # SyntaxError: Missing parentheses in call to 'print'

# Runtime Errors:
# These are exceptions that occur while the program is running.
# They can be caused by end-user input, programming logic, memory problems, and more.
# Exception Handling is used to manage and handle these errors during program execution.

# Example of Runtime Errors:
# Division by zero
print(10 / 0)  # ZeroDivisionError: division by zero

# Unsupported operand types for division
print(10 / "ten")  # TypeError: unsupported operand type(s) for /: 'int' and 'str'

# Value error when trying to convert "ten" to an integer
x = int(input("Enter Number:"))  # Enter Number:ten
print(x)  # ValueError: invalid literal for int() with base 10: 'ten'

# Note:
# Exception Handling concept is applicable for Runtime Errors but not for syntax errors.
