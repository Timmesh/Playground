# __str__() method:
# Whenever we are printing any object reference internally __str__() method will be
# called, which returns a string in the following format:
# <__main__.classname object at 0x022144B0>
# To return a meaningful string representation, we have to override __str__() method.

class Student:
    # Constructor to initialize instance variables
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    # Override the __str__() method to return a custom string representation
    def __str__(self):
        # This method returns a formatted string with student name and roll number.
        return 'This is Student with Name: {} and Rollno: {}'.format(self.name, self.rollno)

# Create two instances of the Student class
s1 = Student('Durga', 101)
s2 = Student('Ravi', 102)

# When we print the objects, the __str__() method is called to display a meaningful representation.
print(s1)
print(s2)
