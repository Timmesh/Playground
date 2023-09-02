# Handling Overloaded Method Requirements in Python

# Class Test with a method sum that can handle different numbers of arguments
class Test:
    # Method sum with default arguments
    def sum(self, a=None, b=None, c=None):
        # If all three arguments are provided
        if a is not None and b is not None and c is not None:
            print('The Sum of 3 Numbers:', a + b + c)
        # If only two arguments are provided
        elif a is not None and b is not None:
            print('The Sum of 2 Numbers:', a + b)
        # If no or less than two arguments are provided
        else:
            print('Please provide 2 or 3 arguments')

# Creating an object of the Test class
t = Test()

# Calling the sum method with different numbers of arguments
t.sum(10, 20)  # Output: The Sum of 2 Numbers: 30
t.sum(10, 20, 30)  # Output: The Sum of 3 Numbers: 60
t.sum(10)  # Output: Please provide 2 or 3 arguments
