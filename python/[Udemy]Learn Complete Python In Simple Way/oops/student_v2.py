## Defining a Class with Properties and Methods:

# A class is a blueprint that defines the properties (attributes) and actions (methods) of objects.
# Here's an example of defining a class 'Student' with properties 'name', 'rollno', and 'marks', and a method 'talk'.

class StudentV2:
    # A special method to initialize the object's properties (attributes).
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    # A method to display the student's information.
    def talk(self):
        print("Hello, My Name is:", self.name)
        print("My Roll Number is:", self.rollno)
        print("My Marks are:", self.marks)
