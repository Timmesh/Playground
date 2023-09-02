class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

class Cow(Animal):
    pass  # Cow inherits Animal's speak method

# Creating instances of different classes
animal = Animal()
dog = Dog()
cat = Cat()
cow = Cow()

# Calling the speak method on different instances
animal.speak()  # Output: Animal speaks
dog.speak()     # Output: Dog barks
cat.speak()     # Output: Cat meows
cow.speak()     # Output: Animal speaks (Inherited from Animal class)
