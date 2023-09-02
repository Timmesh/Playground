# mycalculatormodule.py

# Variable in the module
x = 888
print("My Calculator")
# Function to perform addition
def add(a, b):
    print("The Sum:", a + b)

# Function to perform multiplication
def product(a, b):
    print("The Product:", a * b)

# Function to perform subtraction
def subtract(a, b):
    print("The Difference:", a - b)

# Function to perform division
def divide(a, b):
    if b != 0:
        print("The Division:", a / b)
    else:
        print("Cannot divide by zero!")

