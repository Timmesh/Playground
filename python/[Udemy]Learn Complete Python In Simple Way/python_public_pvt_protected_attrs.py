# By default, every attribute is public. It can be accessed from anywhere.
# Here, we define three attributes: x, _y, and __z.
class Test:
    x = 10      # Public attribute
    _y = 20     # Protected attribute (convention, not enforced)
    __z = 30    # Private attribute

    # A method within the class to demonstrate attribute access
    def m1(self):
        # Accessing public attribute x from within the class is straightforward.
        print(Test.x)

        # Protected attributes (_y) can be accessed within the class without any issues.
        # However, it's a convention to indicate that it should not be accessed from outside the class.
        print(Test._y)

        # Private attributes (__z) can also be accessed within the class.
        # However, it's not recommended to access them from outside the class.
        print(Test.__z)

# Create an instance of the Test class
t = Test()

# Call the m1 method to access the attributes from within the class
t.m1()

# Accessing attributes from outside the class:
# Public attributes (x) can be accessed directly.
print(Test.x)

# Protected attributes (_y) can be accessed from outside the class.
# However, it's a convention that they should not be accessed this way.
print(Test._y)

# Private attributes (__z) cannot be accessed directly from outside the class.
# Attempting to do so will result in an AttributeError.
# Uncomment the line below to see the error.
# print(Test.__z)
