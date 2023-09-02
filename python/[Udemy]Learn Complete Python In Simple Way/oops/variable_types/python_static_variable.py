# Static Variables:
# If the value of a variable is not varied from object to object,
# such type of variables we have to declare within the class directly but outside of methods.
# Such types of variables are called Static variables.
# For the entire class, only one copy of the static variable will be created and shared by all objects of that class.
# We can access static variables either by class name or by object reference. But it is recommended to use the class name.

class Test:
    x = 10  # Static variable

    def __init__(self):
        self.y = 20  # Instance variable

t1 = Test()
t2 = Test()

# Accessing static and instance variables using object references
print('t1:', t1.x, t1.y)  # t1: 10 20
print('t2:', t2.x, t2.y)  # t2: 10 20

# Modifying static and instance variables using object references
Test.x = 888
t1.y = 999

# Accessing modified static and instance variables using object references
print('t1:', t1.x, t1.y)  # t1: 888 999
print('t2:', t2.x, t2.y)  # t2: 888 20
