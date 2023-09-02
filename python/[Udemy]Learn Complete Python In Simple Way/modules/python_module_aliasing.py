# Renaming a Module at the time of import (Module Aliasing)

# When importing a module, you can provide an alternative name, known as an alias, to refer to the module.
# This can be helpful to simplify long module names or avoid naming conflicts.

# Example:
# Importing the module 'mycalculatormodule' and renaming it as 'm'

# Aliasing a module: import original_module_name as alias_name
import mycalculatormodule as m

# Accessing members from the aliased module using the alias name
print(m.x)  # Output: Value of x from 'durgamath' module

# Calling functions from the aliased module
m.add(10, 20)  # Output: Sum of 10 and 20
m.product(10, 20)  # Output: Product of 10 and 20
