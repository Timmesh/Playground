from abc import ABC, abstractmethod


class Shape(ABC):  # Inherits from ABC (Abstract Base Class)
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# You cannot create an instance of Shape directly because it's an abstract class
# shape = Shape()  # This will raise an error

circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle Area:", circle.area())  # Output: Circle Area: 78.53975
print("Rectangle Area:", rectangle.area())  # Output: Rectangle Area: 24
