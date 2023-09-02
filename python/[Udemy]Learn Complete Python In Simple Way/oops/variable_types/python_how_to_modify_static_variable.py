# Modifying the Value of Static Variable:

class Test:
    a = 777

    @classmethod
    def m1(cls):
        cls.a = 888  # Modifying static variable inside classmethod using cls variable

    @staticmethod
    def m2():
        Test.a = 999  # Modifying static variable inside staticmethod using classname

print(Test.a)  # Initial value of static variable: 777

Test.m1()  # Modifying static variable value using class method
print(Test.a)  # Modified value after using class method: 888

Test.m2()  # Modifying static variable value using static method
print(Test.a)  # Modified value after using static method: 999
