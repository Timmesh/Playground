# Instance Methods:

# Inside method implementation, if we are using instance variables, then such type of methods are called instance methods.
# Inside instance method declaration, we have to pass the 'self' variable, like def m1(self):
# By using the 'self' variable inside the method, we can access instance variables.
# Within the class, we can call instance methods using the 'self' variable, and from outside of the class, we can call them using object reference.

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print('Hi', self.name)
        print('Your Marks are:', self.marks)

    def grade(self):
        if self.marks >= 60:
            print('You got First Grade')
        elif self.marks >= 50:
            print('You got Second Grade')
        elif self.marks >= 35:
            print('You got Third Grade')
        else:
            print('You are Failed')

n = int(input('Enter number of students:'))
for i in range(n):
    name = input('Enter Name:')
    marks = int(input('Enter Marks:'))
    s = Student(name, marks)
    s.display()
    s.grade()
    print()

# Setter and Getter Methods:
# We can set and get the values of instance variables by using getter and setter methods.
# Setter Method:
# Setter methods can be used to set values to the instance variables. Setter methods are also known as mutator methods.
# Syntax: def setVariable(self, variable): self.variable = variable
# Getter Method:
# Getter methods can be used to get values of the instance variables. Getter methods are also known as accessor methods.
# Syntax: def getVariable(self): return self.variable

class Student:

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

n = int(input('Enter number of students:'))
for i in range(n):
    s = Student()
    name = input('Enter Name:')
    s.setName(name)
    marks = int(input('Enter Marks:'))
    s.setMarks(marks)
    print('Hi', s.getName())
    print('Your Marks are:', s.getMarks())
    print()
