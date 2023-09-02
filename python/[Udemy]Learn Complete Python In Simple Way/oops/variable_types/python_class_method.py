# Class Methods:
# Inside method implementation if we are using only class variables (static variables),
# then such type of methods we should declare as class method.
# We can declare class method explicitly by using @classmethod decorator.
# For class method, we should provide cls variable at the time of declaration.
# We can call class method by using the class name or object reference variable.

class Animal:
    legs = 4  # Class variable

    @classmethod
    def walk(cls, name):
        print('{} walks with {} legs...'.format(name, cls.legs))
        print(id(cls))

# Calling the class method using the class name
Animal.walk('Dog')  # Dog walks with 4 legs...
Animal.walk('Cat')  # Cat walks with 4 legs...
print(id(Animal))