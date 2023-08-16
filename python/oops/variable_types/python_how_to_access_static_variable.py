# Accessing Static Variables in Different Contexts:

class Test:
    a = 10  # Static variable declared directly in class

    def __init__(self):
        print(self.a)  # Accessing static variable inside constructor using self
        print(Test.a)  # Accessing static variable inside constructor using classname

    def m1(self):
        print(self.a)  # Accessing static variable inside instance method using self
        print(Test.a)  # Accessing static variable inside instance method using classname

    @classmethod
    def m2(cls):
        print(cls.a)  # Accessing static variable inside classmethod using cls variable
        print(Test.a)  # Accessing static variable inside classmethod using classname

    @staticmethod
    def m3():
        print(Test.a)  # Accessing static variable inside staticmethod using classname

t = Test()

print(Test.a)  # Accessing static variable outside the class using classname
print(t.a)  # Accessing static variable outside the class using object reference

t.m1()  # Accessing static variable inside instance method
t.m2()  # Accessing static variable inside class method
t.m3()  # Accessing static variable inside static method
