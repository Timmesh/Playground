## Everything is an Object

# Introduction to the concept that everything in Python is an object.
# - In Python, every entity, including integers, strings, functions, etc., is treated as an object.

# Even functions are objects
# - Functions are not an exception; they are also treated as objects internally.

# Example: Functions as objects

def f1():
    print("Hello")

# Displaying the function object
print(f1)  # <function f1 at 0x00419618>

# Displaying the memory address of the function object
print(id(f1))  # 4298264

# Explanation:
# - In Python, functions are first-class citizens, which means they can be assigned to variables, passed as arguments to other functions, and returned as values from other functions.
# - In the example, the function 'f1' is defined and displayed as an object using 'print(f1)'.
# - The memory address of the function object is obtained using 'id(f1)' and displayed using 'print(id(f1))'.
# - This demonstrates that functions are treated as objects, and their memory locations can be accessed just like any other objects.

