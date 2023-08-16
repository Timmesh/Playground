# Inside Instance Method by using Self Variable:

# We can also declare instance variables inside an instance method by using the self variable.
# If any instance variable is declared inside an instance method, that instance variable will be added to the object
# once we call that method.

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30

t = Test()
print(t.__dict__)  # {'a': 10, 'b': 20}
t.m1()
print(t.__dict__)  # {'a': 10, 'b': 20, 'c': 30}
