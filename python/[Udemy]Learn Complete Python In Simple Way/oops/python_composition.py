# By Composition (Has-A Relationship):
# By using Class Name or by creating an object we can access members of one class inside
# another class, which is called composition (Has-A Relationship).
# The main advantage of Has-A Relationship is Code Reusability.

class Engine:
    a = 10
    def __init__(self):
        self.b = 20

    def m1(self):
        print('Engine Specific Functionality')

class Car:
    def __init__(self):
        self.engine = Engine()

    def m2(self):
        print('Car using Engine Class Functionality')
        print(self.engine.a)   # Accessing Engine's class variable
        print(self.engine.b)   # Accessing Engine's instance variable
        self.engine.m1()       # Accessing Engine's method

c = Car()
c.m2()

# Demo Program-2:
class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def getinfo(self):
        print("Car Name: {}, Model: {} and Color: {}".format(self.name, self.model, self.color))

class Employee:
    def __init__(self, ename, eno, car):
        self.ename = ename
        self.eno = eno
        self.car = car

    def empinfo(self):
        print("Employee Name:", self.ename)
        print("Employee Number:", self.eno)
        print("Employee Car Info:")
        self.car.getinfo()

c = Car("Innova", "2.5V", "Grey")
e = Employee('Durga', 10000, c)
e.empinfo()

# Demo Program-3:
class X:
    a = 10
    def __init__(self):
        self.b = 20

    def m1(self):
        print("m1 method of X class")

class Y:
    c = 30
    def __init__(self):
        self.d = 40

    def m2(self):
        print("m2 method of Y class")

    def m3(self):
        x1 = X()
        print(x1.a)   # Accessing X's class variable
        print(x1.b)   # Accessing X's instance variable
        x1.m1()       # Accessing X's method
        print(Y.c)    # Accessing Y's class variable
        print(self.d) # Accessing Y's instance variable
        self.m2()     # Accessing Y's method
        print("m3 method of Y class")

y1 = Y()
y1.m3()
