# Constructor Overloading in Python

# Class Test with multiple __init__ methods, attempting constructor overloading
class Test:
    # Last __init__ method will be considered
    def __init__(self):
        print('No-Arg Constructor')

    def __init__(self, a):
        print('One-Arg constructor')

    def __init__(self, a, b):
        print('Two-Arg constructor')

# Attempting to create an object of the Test class with different numbers of arguments
# Only the last __init__ method is considered
# t1 = Test()  # This line will raise an error due to missing arguments
# t1 = Test(10)  # This line will raise an error due to missing arguments
t1 = Test(10, 20)  # Output: Two-Arg constructor
