# Instance Variables:

# If the value of a variable is varied from object to object, then such type of variables are called instance variables.
# For every object, a separate copy of instance variables will be created.
# We can declare instance variables in the following ways:

class Employee:
    def __init__(self, ename, eid):
        self.name = ename  # Inside Constructor using self variable
        self.id = eid

    def display(self):
        self.salary = 10000  # Inside Instance Method using self variable
        print("Name:", self.name)
        print("ID:", self.id)
        print("Salary:", self.salary)

e1 = Employee("John", 101)
e2 = Employee("Alice", 102)

e1.display()  # Name: John  ID: 101  Salary: 10000
e2.display()  # Name: Alice  ID: 102  Salary: 10000

e1.salary = 15000  # Outside the class using object reference variable
print("Salary of", e1.name, ":", e1.salary)  # Salary of John : 15000

e1.role = "Senior S/W Engineer"  # Adding a new instance variable
print(e1.__dict__)  # {'name': 'John', 'id': 101, 'salary': 15000, 'role': 'Senior S/W Engineer'}
print(e2.__dict__)  # {'name': 'Alice', 'id': 102, 'salary': 10000}

