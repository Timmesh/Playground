# Example of Inheritance and Method Overriding
# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eatndrink(self):
        print('Eat Biryani and Drink Beer')

# Child Class inheriting from Person Class
class Employee(Person):
    def __init__(self, name, age, eno, esal):
        super().__init__(name, age)  # Calling Parent class constructor
        self.eno = eno
        self.esal = esal

    def work(self):
        print("Coding Python is very easy just like drinking Chilled Beer")

    def empinfo(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee Number:", self.eno)
        print("Employee Salary:", self.esal)

# Creating an object of Child Class
e = Employee('Durga', 48, 100, 10000)
e.eatndrink()  # Output: Eat Biryani and Drink Beer (Inherited from Person)
e.work()  # Output: Coding Python is very easy just like drinking Chilled Beer
e.empinfo()  # Output: Employee Details