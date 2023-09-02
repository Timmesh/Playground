# Method Overloading Explanation
# Method overloading refers to defining multiple methods with the same name but different parameters.
# In some programming languages, method overloading allows selecting a method based on the number or type of arguments.

# Class Test with multiple methods having the same name
class Test:
    # Defining a method m1 with no arguments
    def m1(self):
        print('no-arg method')

    # Redefining the method m1 with one argument (overwriting the previous method)
    def m1(self, a):
        print('one-arg method')

    # Redefining the method m1 with two arguments (overwriting the previous methods)
    def m1(self, a, b):
        print('two-arg method')

# Creating an object of the Test class
t = Test()

# Uncommenting each line below and running the code will result in an AttributeError due to method overwriting.
# t.m1()  # AttributeError: 'Test' object has no attribute 'm1' with no arguments
# t.m1(10)  # AttributeError: 'Test' object has no attribute 'm1' with one argument

# Calling the last defined method m1 with two arguments
t.m1(10, 20)
