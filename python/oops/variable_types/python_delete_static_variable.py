# Deleting Static Variables of a Class:

# We can delete static variables from anywhere using either class name or cls variable (inside class method).
# However, we can't modify or delete static variables using object reference variable or self.

# Example 1: Deleting static variable using class name
class Test:
    a = 10

    @classmethod
    def m1(cls):
        del cls.a

Test.m1()
print(Test.__dict__)  # {}

# Example 2: Deleting static variable using class name and cls variable inside classmethod
class Test:
    a = 10

    def __init__(self):
        Test.b = 20
        del Test.a

    def m1(self):
        Test.c = 30
        del Test.b

    @classmethod
    def m2(cls):
        cls.d = 40
        del Test.c

    @staticmethod
    def m3():
        Test.e = 50
        del Test.d

print(Test.__dict__)  # {'a': 10, '__init__': <function Test.__init__ at 0x...}
t = Test()
print(Test.__dict__)  # {'__init__': <function Test.__init__ at 0x...}
t.m1()
print(Test.__dict__)  # {'__init__': <function Test.__init__ at 0x...}
Test.m2()
print(Test.__dict__)  # {'m2': <classmethod object at 0x...}
Test.m3()
print(Test.__dict__)  # {'m2': <classmethod object at 0x...}
Test.f = 60
print(Test.__dict__)  # {'m2': <classmethod object at 0x..., 'f': 60}

# Attempting to read, modify, or delete static variables using object reference or self
class Test:
    a = 10

t1 = Test()
print(t1.a)  # 10 (reading static variable using object reference)
t1.a = 70   # Modifying static variable using object reference (creates an instance variable)
print(t1.a)  # 70 (reading the modified instance variable)
del t1.a    # Attempting to delete using object reference raises AttributeError

# Attempting to delete static variable using object reference raises AttributeError
class Test:
    a = 10

t1 = Test()
del t1.a    # AttributeError: a

# Modifying or deleting static variables can only be done using class name or cls variable.
