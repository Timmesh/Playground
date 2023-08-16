# Command Line Arguments in Python

# Command Line Arguments are the arguments passed to a Python script at the time of its execution.
# The arguments provided on the command line are stored in the list 'argv', which is available in the 'sys' module.

# Example 1: Displaying Command Line Arguments
# Let's create a Python script to display the command line arguments passed to the script.

import sys

print("The Number of Command Line Arguments:", len(sys.argv))
print("The List of Command Line Arguments:", sys.argv)
print("Command Line Arguments one by one:")
for arg in sys.argv:
    print(arg)

# When executing this script with command line arguments, it will display the number of arguments, the list of arguments,
# and then display each argument one by one.

# Example 2: Performing Operations on Command Line Arguments
# We can perform operations on the command line arguments based on our requirements.

from sys import argv

# The command line arguments are strings by default, we can convert them into the required data type using type casting.
arg1 = int(argv[1])
arg2 = int(argv[2])

print("Sum of command line arguments:", arg1 + arg2)
print("Product of command line arguments:", arg1 * arg2)

# Example 3: Handling Command Line Arguments with Spaces
# If the command line argument contains spaces, we can enclose it in double quotes.

# When executing the script with the command line argument "Nakul Timmesh", it will display the entire name correctly.
# Command: python script.py "Nakul Timmesh"

# Example 4: Handling Invalid Command Line Arguments
# If we try to access command line arguments with an out-of-range index, it will raise an IndexError.

# For example, if we only pass one command line argument while the script is expecting two, it will raise an IndexError.

# argparse Module:
# In more complex scenarios where we need to parse command line arguments and provide help messages for incorrect input,
# the argparse module is often used. It provides a more advanced way of handling command line arguments.
# It allows specifying arguments with options, default values, and various types.

# For simple scripts, using sys.argv is sufficient, but for more complex projects, argparse is preferred.

