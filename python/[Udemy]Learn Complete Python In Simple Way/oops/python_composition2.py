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
