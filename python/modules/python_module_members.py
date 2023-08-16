# Various Possibilities of Importing Modules

# Python provides several ways to import modules and their members, giving you flexibility in how you use them.

# Importing specific members from a module using 'from ... import ...'
from mycalculatormodule import x, add

# Accessing members directly without using the module name
print(x)  # Output: Value of x from 'mycalculatormodule' module
add(10, 20)  # Output: Sum of 10 and 20

# However, other members of the module are not directly accessible
# product(10, 20)  # Error: NameError: name 'product' is not defined

# Importing all members of a module using 'from ... import *'
from mycalculatormodule import *

# Now you can directly access all members without the module name
print(x)  # Output: Value of x from 'mycalculatormodule' module
add(10, 20)  # Output: Sum of 10 and 20
product(10, 20)  # Output: Product of 10 and 20
