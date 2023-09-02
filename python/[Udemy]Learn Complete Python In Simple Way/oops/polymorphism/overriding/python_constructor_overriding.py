class Parent:
    def __init__(self, value):
        self.value = value
        print("Parent constructor")

class Child(Parent):
    def __init__(self, value):
        super().__init__(value)
        print("Child constructor")

class GrandChild(Child):
    def __init__(self, value):
        super().__init__(value)
        print("GrandChild constructor")

# Creating instances of different classes
parent = Parent("Parent")
child = Child("Child")
grandchild = GrandChild("GrandChild")
