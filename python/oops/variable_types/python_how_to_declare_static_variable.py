# Various Places to Declare Static Variables:
# Static variables can be declared in various places within a class.
# These static variables are shared among all instances of the class.

class Test:
    x = 10  # Static variable declared outside of any method

    def __init__(self):
        Test.z = 30  # Static variable declared inside constructor using class name

    def display(self):
        Test.y = 20  # Static variable declared inside instance method using class name

    @classmethod
    def modify(cls):
        cls.m = 40  # Static variable declared inside classmethod using cls variable
        Test.n = 50  # Static variable declared inside classmethod using class name

    @staticmethod
    def calc():
        Test.p = 60  # Static variable declared inside staticmethod using class name

# Creating objects to trigger the declarations
t1 = Test()
t1.display()
Test.modify()
Test.calc()

# Accessing the static variables declared in different places
print(Test.x)  # Accessing static variable declared outside of any method: 10
print(Test.z)  # Accessing static variable declared inside constructor: 30
print(Test.y)  # Accessing static variable declared inside instance method: 20
print(Test.m)  # Accessing static variable declared inside classmethod using cls variable: 40
print(Test.n)  # Accessing static variable declared inside classmethod using class name: 50
print(Test.p)  # Accessing static variable declared inside staticmethod: 60
