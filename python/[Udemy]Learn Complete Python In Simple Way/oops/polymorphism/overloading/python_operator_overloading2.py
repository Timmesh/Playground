# Defining a class named Student
class Student:
    # Constructor to initialize name and marks
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Overloading the > operator to compare Student objects based on marks
    def __gt__(self, other):
        return self.marks > other.marks

    # Overloading the <= operator to compare Student objects based on marks
    def __le__(self, other):
        return self.marks <= other.marks

# Testing the overloading of operators
# Comparing integers using the > operator
print("10 > 20 =", 10 > 20)

# Creating Student objects
s1 = Student("Durga", 100)
s2 = Student("Ravi", 200)

# Comparing Student objects using the >, <, <=, and >= operators
print("s1 > s2 =", s1 > s2)
print("s1 < s2 =", s1 < s2)
print("s1 <= s2 =", s1 <= s2)
print("s1 >= s2 =", s1 >= s2)
