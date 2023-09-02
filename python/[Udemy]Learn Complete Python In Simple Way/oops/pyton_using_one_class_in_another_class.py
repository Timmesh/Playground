# Using Members of One Class inside Another Class

# 1. By Composition (Has-A Relationship)
# In this approach, one class contains an instance of another class as its member.
# This is also known as composition or aggregation.

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        print("Car is being driven")

c = Car()
c.drive()  # Car is being driven
c.engine.start()  # Engine started


# 2. By Inheritance (IS-A Relationship)
# In this approach, one class inherits from another class.
# This is also known as an inheritance relationship.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

d = Dog()
d.speak()  # Dog barks

c = Cat()
c.speak()  # Cat meows
