# Running Other Programs from a Python Program:

# The 'os' module contains the 'system()' function, which is used to run external programs and commands.
# It is similar to the 'system()' function in the C language.

# To run an external command or program, use the 'os.system("command string")' syntax.

# Example:
import os

# Running an external command to list all Python files in the current directory.
os.system("dir input_output_statements\*.py")

# Running an external Python script named 'abc.py'.
os.system("py test.py")

# Note: The argument to 'os.system()' is a command string that can execute any valid command or program in the terminal.
