# Types of Methods:

# Inside a Python class, three types of methods are allowed:
# 1. Instance Methods
# 2. Class Methods
# 3. Static Methods

class MyClass:

    # Instance Method:
    # Inside method implementation, if we are using instance variables, then such type of methods are called instance methods.
    # Inside instance method declaration, we have to pass 'self' variable: def instance_method(self)
    # By using 'self' variable inside the method, we can access instance variables.
    # Within the class, we can call instance methods using the 'self' variable and from outside of the class, we can call them using object reference.

    def instance_method(self):
        print("This is an instance method.")

    # Class Method:
    # If a method is related to class but not related to instance variables, it's a class method.
    # Class methods are defined using the @classmethod decorator.
    # They accept the class as their first parameter, commonly named 'cls'.
    # Class methods can access and modify class-level attributes.
    # They can be called using the class name or an instance of the class.

    @classmethod
    def class_method(cls):
        print("This is a class method.")

    # Static Method:
    # Static methods are not tied to either instance variables or class-level attributes.
    # They are defined using the @staticmethod decorator.
    # Static methods don't take 'self' or 'cls' as their first parameter.
    # They can be called using the class name or an instance of the class.

    @staticmethod
    def static_method():
        print("This is a static method.")

# Creating an instance of the class
obj = MyClass()

# Calling different types of methods
obj.instance_method()  # This is an instance method.
MyClass.class_method()  # This is a class method.
obj.class_method()  # This is a class method.
MyClass.static_method()  # This is a static method.
obj.static_method()  # This is a static method.
