# Outside of the Class by using Object Reference Variable:

# We can also add instance variables outside of a class to a particular object.

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30

t = Test()
t.m1()
print(t.__dict__)  # {'a': 10, 'b': 20, 'c': 30}

t.d = 40  # Adding an instance variable 'd' to object 't'
print(t.__dict__)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
