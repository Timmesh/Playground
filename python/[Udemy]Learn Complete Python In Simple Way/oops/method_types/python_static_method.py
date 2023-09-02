# Static Methods:

# Static methods are usually used as general utility methods.
# Inside these methods, we won't use any instance or class variables.
# No 'self' or 'cls' arguments are provided at the time of declaration.
# Static methods are declared using the @staticmethod decorator.
# Static methods can be accessed using the classname or object reference.

class MyMath:

    @staticmethod
    def add(x, y):
        print('The Sum:', x + y)

    @staticmethod
    def product(x, y):
        print('The Product:', x * y)

    @staticmethod
    def average(x, y):
        print('The average:', (x + y) / 2)

# Using the static methods of the MyMath class
MyMath.add(10, 20)         # The Sum: 30
MyMath.product(10, 20)    # The Product: 200
MyMath.average(10, 20)    # The average: 15.0
