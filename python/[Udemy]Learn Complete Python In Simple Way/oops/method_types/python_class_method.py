# Class Methods:

# Inside method implementation, if we are using only class variables (static variables), then such type of methods should be declared as class methods.
# We can declare a class method explicitly by using the @classmethod decorator.
# For class methods, we should provide 'cls' variable at the time of declaration.
# We can call a class method using the classname or object reference variable.

class Animal:
    legs = 4

    @classmethod
    def walk(cls, name):
        print('{} walks with {} legs...'.format(name, cls.legs))

Animal.walk('Dog')  # Dog walks with 4 legs...
Animal.walk('Cat')  # Cat walks with 4 legs...

# Program to track the Number of Objects created for a Class:

class Test:
    count = 0

    def __init__(self):
        Test.count = Test.count + 1

    @classmethod
    def noOfObjects(cls):
        print('The number of objects created for test class:', cls.count)

t1 = Test()
t2 = Test()
Test.noOfObjects()
t3 = Test()
t4 = Test()
t5 = Test()
Test.noOfObjects()
