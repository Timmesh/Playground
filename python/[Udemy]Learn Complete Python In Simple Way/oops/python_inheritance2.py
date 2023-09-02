# Parent Class
class P:
    a = 10

    def __init__(self):
        self.b = 10

    def m1(self):
        print('Parent instance method')

    @classmethod
    def m2(cls):
        print('Parent class method')

    @staticmethod
    def m3():
        print('Parent static method')

# Child Class inheriting from Parent Class
class C(P):
    c = 30

    def __init__(self):
        super().__init__()  # Calling Parent class constructor
        self.d = 30

# Creating an object of Child Class
c1 = C()
print(c1.a)  # Output: 10 (Inherited from Parent)
print(c1.b)  # Output: 10 (Inherited from Parent)
print(c1.c)  # Output: 30 (Child's own attribute)
print(c1.d)  # Output: 30 (Child's own attribute)