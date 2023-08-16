# Declaring Static Variables in Different Methods:

class Test:
    a = 10  # Static variable declared directly in class

    def __init__(self):
        Test.b = 20  # Static variable declared inside constructor

    def m1(self):
        Test.c = 30  # Static variable declared inside instance method

    @classmethod
    def m2(cls):
        cls.d1 = 40  # Static variable declared inside classmethod using cls variable
        Test.d2 = 400  # Static variable declared inside classmethod using class name

    @staticmethod
    def m3():
        Test.e = 50  # Static variable declared inside staticmethod

# Initial state of the class dictionary
print(Test.__dict__)  # {}

# Creating an object of the class
t = Test()

# State of the class dictionary after creating an object
print(Test.__dict__)  # {'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x7f8bb826d670>, ...}

# Calling instance method m1
t.m1()

# State of the class dictionary after calling instance method m1
print(Test.__dict__)  # {'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x7f8bb826d670>, ...}

# Calling class method m2
Test.m2()

# State of the class dictionary after calling class method m2
print(Test.__dict__)  # {'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x7f8bb826d670>, ...}

# Calling static method m3
Test.m3()

# State of the class dictionary after calling static method m3
print(Test.__dict__)  # {'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x7f8bb826d670>, ...}

# Adding a new static variable directly to the class
Test.f = 60

# State of the class dictionary after adding a new static variable
print(Test.__dict__)  # {'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x7f8bb826d670>, ...}
