# Define the parent class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('Name:', self.name)
        print('Age:', self.age)

# Define the child class Student inheriting from Person
class Student(Person):
    def __init__(self, name, age, rollno, marks):
        # Using super() to call the constructor of the parent class Person
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks

    # Override the display method to add more functionality
    def display(self):
        # Calling the display method of the parent class using super()
        super().display()
        print('Roll No:', self.rollno)
        print('Marks:', self.marks)

# Create an instance of the Student class
s1 = Student('Durga', 22, 101, 90)

# Call the display method of the Student instance
s1.display()
