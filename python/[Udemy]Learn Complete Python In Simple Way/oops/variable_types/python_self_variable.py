## The 'self' Variable in Python:

# In Python, the 'self' variable is used to refer to the current object within a class's methods.
# It acts similar to the 'this' keyword in Java.
# It allows us to access instance variables and instance methods of the object.

class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def talk(self):
        print("Hello, My Name is:", self.name)
        print("My Roll Number is:", self.rollno)
        print("My Marks are:", self.marks)

# Creating objects of the Student class
s1 = Student("Alice", 101, 95)
s2 = Student("Bob", 102, 85)

# Calling the 'talk' method on the objects
s1.talk()  # Output:
# Hello, My Name is: Alice
# My Roll Number is: 101
# My Marks are: 95

s2.talk()  # Output:
# Hello, My Name is: Bob
# My Roll Number is: 102
# My Marks are: 85
