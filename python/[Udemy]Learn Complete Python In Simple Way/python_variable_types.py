# Types of Variables in Python
# Global Variables and Local Variables

# Global Variables
# Variables declared outside functions are global variables
a = 10  # global variable

def f1():
    print(a)

def f2():
    print(a)

f1()  # Output: 10
f2()  # Output: 10

# Local Variables
# Variables declared inside functions are local variables
def f1():
    a = 10
    print(a)  # Valid

def f2():
    print(a)  # Invalid, NameError: name 'a' is not defined

f1()
f2()
# Output:
# 10
# NameError: name 'a' is not defined

# Using the global Keyword
# We can use the global keyword to declare and access global variables inside functions

a = 10

def f1():
    a = 777  # Local variable with the same name
    print(a)  # Output: 777

def f2():
    print(a)  # Output: 10

f1()
f2()

def f1():
    global a
    a = 777  # Changes the global variable value
    print(a)  # Output: 777

def f2():
    print(a)  # Output: 777

f1()
f2()

# Accessing Global Variable with Local Variable of the Same Name
a = 10  # Global Variable

def f1():
    a = 777  # Local Variable
    print(a)  # Output: 777
    print(globals()['a'])  # Output: 10

f1()

def f1():
    a = 777  # Local Variable
    print(a)  # Output: 777
    globals()['a'] = 100
    print(globals()['a'])  # Output: 100

f1()


# Summary:
# - Python supports global and local variables.
# - Global variables are declared outside functions and can be accessed in all functions of the module.
# - Local variables are declared inside functions and are available only within that function.
# - The global keyword is used to declare global variables inside functions and to make global variables available for modification.
# - If a global variable and a local variable have the same name, the global variable can be accessed within a function using globals()['variable_name'].
