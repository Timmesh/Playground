# Composition vs Aggregation

# Composition Example
# University and Department have a strong relationship, as Department cannot exist without University.
class University:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name):
        self.name = name

# Aggregation Example
# Professor can exist without Department, so the relationship between Professor and Department is weak.
class Professor:
    def __init__(self, name):
        self.name = name

# Coding Example
class Student:
    collegeName = 'DURGASOFT'  # Static variable

    def __init__(self, name):
        self.name = name
        print(Student.collegeName)  # Aggregation
        s = Student('Durga')
        print(s.name)  # Composition

# In the above example, Student object and its name are strongly associated (Composition).
# Student object and collegeName are weakly associated (Aggregation).

# Conclusion: The relation between an object and its instance variables is always Composition,
# whereas the relation between an object and static variables is Aggregation.
