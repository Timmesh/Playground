# Inner Classes

# Inner classes are classes declared inside another class.
# Inner classes are used when one type of object cannot exist without another type of object.
# For example, an Engine class should be part of a Car class, and a Department class should be part of a University class.

# Outer class definition
class Outer:
    def __init__(self):
        print("Outer class object creation")

    # Inner class definition
    class Inner:
        def __init__(self):
            print("Inner class object creation")

        def m1(self):
            print("Inner class method")

# Creating an object of the Outer class
o = Outer()             # Outer class object creation

# Creating an object of the Inner class using the Outer class object
i = o.Inner()           # Inner class object creation

# Calling the method of the Inner class using the Inner class object
i.m1()                  # Inner class method
