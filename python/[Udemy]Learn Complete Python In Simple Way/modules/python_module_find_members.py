# Finding Members of a Module using dir() Function

# Python provides the built-in function dir() to list all members of the current module or a specified module.

# Listing members of the current module
x = 10
y = 20
def f1():
    print("Hello")
    print(dir())  # This lists all members of the current module

# Output:
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', 'f1', 'x', 'y']

# By calling dir() within the module, you can see all its members, including built-in properties.

# Listing members of a particular module


# In your program:
import mycalculatormodule
print(dir(mycalculatormodule))

# Output:
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__spec__', 'add', 'product', 'x']

# The dir() function also includes special properties that Python interpreter adds automatically for internal use.
# These properties can be accessed based on our requirements.

# For example:
print(__builtins__)
print(__cached__)
print(__doc__)
print(__file__)
print(__loader__)
print(__name__)
print(__package__)
print(__spec__)
