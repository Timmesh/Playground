# Inheritance and Constructors

# Parent class P
class P:
    def __init__(self):
        print("Parent Constructor executed. Object ID:", id(self))

# Child class C inheriting from P
class C(P):
    pass

c = C()  # Creating a child class object

print("Child Object ID:", id(c))

# When a child class object is created, the constructor of the child class is executed.
# In this example, the constructor of class P is executed because class C does not have its own constructor.
# The id(self) shows that the same object is being used in both constructors.