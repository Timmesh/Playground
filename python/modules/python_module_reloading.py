# Reloading a Module in Python

# By default, a module in Python is loaded only once, even if it's imported multiple times.
# However, this can lead to issues if you make changes to the module outside your program and want the updated version.

# Consider the following scenario:
# [module1.py]:
# print("This is from module1")

# In your main program [test.py]:
# import module1
# import module1
# import module1
# import module1
# print("This is test module")

# Output:
# This is from module1
# This is test module

# In the above program, the module 'module1' is imported multiple times, but it's loaded only once by default.
# If you update 'module1' externally, the changes won't be reflected in your program.

# To solve this problem, you can explicitly reload a module using the reload() function from the 'imp' module.

# Explicitly reloading a module
import importlib
import mycalculatormodule
importlib.reload(mycalculatormodule)

# Alternatively, you can use the 'reload' function directly after importing it
from importlib import reload
import mycalculatormodule
reload(mycalculatormodule)
reload(mycalculatormodule)
reload(mycalculatormodule)

# Now the 'module1' will be reloaded explicitly each time, ensuring that any updates are reflected in your program.
# This is especially useful when you're actively working on a module and need the latest version in your program.
# The output will show the updated module content each time it's reloaded.
