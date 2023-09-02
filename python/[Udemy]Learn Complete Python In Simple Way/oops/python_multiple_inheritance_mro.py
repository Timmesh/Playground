# Multiple Inheritance and Method Resolution Order (MRO) in Python

# Parent class P1
class P1:
    def m1(self):
        print("Parent1 Method")

# Parent class P2
class P2:
    def m1(self):
        print("Parent2 Method")

# Child class C inheriting from both P1 and P2
class C(P1, P2):
    def m2(self):
        print("Child Method")

# Creating an object of the child class C
c = C()

# Accessing methods from parent classes and child class
c.m1()  # Calls m1 from P1 class (order of P1 and P2 matters)
c.m2()  # Calls m2 from Child class
