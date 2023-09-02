# Member Aliasing in Python

# In Python, you can give an alias name to members imported from a module to provide a different name for convenience.

# Importing specific members with aliasing
from mycalculatormodule import x as y, add as sum

# Using the alias names to access the members
print(y)      # Output: Value of x from 'mycalculatormodule' module
sum(10, 20)   # Output: Sum of 10 and 20

# Aliasing allows you to use a different name for the imported members.
# Here, 'x' from 'mycalculatormodule' module is imported as 'y'.
# Similarly, 'add' from 'mycalculatormodule' module is imported as 'sum'.

# Attempting to use the original name instead of the alias name results in an error
# print(x)  # Error: NameError: name 'x' is not defined
