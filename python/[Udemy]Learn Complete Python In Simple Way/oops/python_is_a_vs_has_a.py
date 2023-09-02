# IS-A vs HAS-A Relationship

# IS-A Relationship Example
# Person is a parent class, and Employee is a child class extending its functionality.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eatndrink(self):
        print('Eat Biryani and Drink Beer')

class Employee(Person):
    def __init__(self, name, age, eno, esal, car):
        super().__init__(name, age)  # Inheriting from Person
        self.eno = eno
        self.esal = esal
        self.car = car

    def work(self):
        print("Coding Python is very easy just like drinking Chilled Beer")

    def empinfo(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee Number:", self.eno)
        print("Employee Salary:", self.esal)
        print("Employee Car Info:")
        self.car.getinfo()

# Car class to demonstrate HAS-A Relationship
class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def getinfo(self):
        print("\tCar Name:{} \n\t Model:{} \n\t Color:{}".format(self.name, self.model, self.color))

# Creating Car and Employee objects
c = Car("Innova", "2.5V", "Grey")
e = Employee('Durga', 48, 100, 10000, c)

# Using Employee's functionality
e.eatndrink()  # Output: Eat Biryani and Drink Beer
e.work()  # Output: Coding Python is very easy just like drinking Chilled Beer
e.empinfo()  # Output: Employee Details along with Car Info
