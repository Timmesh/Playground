# Constructor Concept:

# Constructor is a special method in Python.
# The name of the constructor should be __init__(self)
# Constructor will be executed automatically at the time of object creation.
# The main purpose of the constructor is to declare and initialize instance variables.
# Per object, the constructor will be executed only once.
# Constructor can take at least one argument (at least self).
# Constructor is optional and if we are not providing any constructor then Python will provide the default constructor.

class Student:
    '''This is the student class with required data'''
    def __init__(self, x, y, z):
        self.name = x
        self.rollno = y
        self.marks = z

    def display(self):
        print("Student Name: {}\nRollno: {} \nMarks: {}".format(self.name, self.rollno, self.marks))

# Creating instances of the Student class
s1 = Student("Durga", 101, 80)
s1.display()  # Student Name: Durga Rollno: 101 Marks: 80

s2 = Student("Sunny", 102, 100)
s2.display()  # Student Name: Sunny Rollno: 102 Marks: 100
