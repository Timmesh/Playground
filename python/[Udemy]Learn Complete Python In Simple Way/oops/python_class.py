## What is Class:

# In Python, everything is an object. To create objects, we require a model or blueprint, which is known as a class.
# A class is used to represent the properties (attributes) and actions (behavior) of an object.
# Properties are represented by variables, and actions are represented by methods.
# Therefore, a class contains both variables and methods.

### How to Define a Class?

# We can define a class using the class keyword.

# Syntax:
# class ClassName:
#       ''' documentation string '''
#       variables: instance variables, static and local variables
#       methods: instance methods, static methods, class methods

# Documentation string represents a description of the class. It's optional but useful for documentation.
# You can access the doc string using print(classname.__doc__) or help(classname).

# Within a Python class, we can represent data using variables. There are three types of variables allowed:
# 1. Instance Variables (Object Level Variables)
# 2. Static Variables (Class Level Variables)
# 3. Local Variables (Method Level Variables)

# Within a Python class, we can represent operations using methods. Various types of allowed methods are:
# 1. Instance Methods
# 2. Class Methods
# 3. Static Methods

from student import Student
from student_v2 import StudentV2

s = Student()
print(s.name)
s.talk()

s1 = StudentV2("Naku",1,99)
print(s1.name)
s1.talk()


# What is Object:

# An object is the physical existence of a class. It's an instance of a class. We can create any number of objects for a class.

# Syntax to Create Object:
# referencevariable = classname()

# For example:
# s = Student()

## What is Reference Variable?

# The variable that can be used to refer to an object is called a reference variable.
# By using a reference variable, we can access properties and methods of an object.


# Here, 's' is the reference variable that refers to the object of the Student class.
# Using this reference variable, we can access the properties and methods of the object.
