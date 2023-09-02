# Define the Parent class P
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

# Define the Child class C inheriting from Parent class P
class C(P):
    a = 888
    def __init__(self):
        self.b = 999
        # Using super() to call the constructor of the Parent class P
        super().__init__()
        # Using super() to access the class attributes and methods of Parent class P
        print(super().a)
        super().m1()
        super().m2()
        super().m3()

# Create an instance of the Child class C
c = C()
