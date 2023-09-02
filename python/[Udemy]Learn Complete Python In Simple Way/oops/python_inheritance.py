# By Inheritance (IS-A Relationship):
# Whatever variables, methods, and constructors available in the parent class are
# by default available to the child classes without rewriting.
# The main advantage of inheritance is Code Reusability, and we can extend existing
# functionality with some more extra functionality.

# Parent Class
class Parent:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

# Child Class inheriting from Parent Class
class Child(Parent):
    def __init__(self, name, age):
        # Calling the parent class constructor using super()
        super().__init__(name)
        self.age = age

    def display(self):
        # Calling the parent class method using super()
        super().display()
        print("Age:", self.age)

# Creating objects
p = Parent("John")
c = Child("Alice", 25)

# Calling methods
print("Parent Object:")
p.display()  # Output: Name: John

print("\nChild Object:")
c.display()  # Output: Name: Alice, Age: 25
