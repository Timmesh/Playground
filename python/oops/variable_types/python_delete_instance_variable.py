# How to Delete Instance Variable from the Object:
# 1. Within a class, we can delete instance variables using del self.variableName.
# 2. From outside the class, we can delete instance variables using del objectreference.variableName.

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def m1(self):
        del self.d


t = Test()
print(t.__dict__)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40}
t.m1()
print(t.__dict__)  # {'a': 10, 'b': 20, 'c': 30}
del t.c
print(t.__dict__)  # {'a': 10, 'b': 20}


# Note:
# Deleted instance variables from one object won't be deleted from other objects.
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20


t1 = Test()
t2 = Test()
del t1.a
print(t1.__dict__)  # {'b': 20}
print(t2.__dict__)  # {'a': 10, 'b': 20}


# Changes to instance variables of one object won't be reflected in other objects.
class Test:
    def __init__(self):
        self.a = 100
        self.b = 200


t1 = Test()
t1.a = 888
t1.b = 999
t2 = Test()
print('t1:', t1.a, t1.b)  # t1: 888 999
print('t2:', t2.a, t2.b)  # t2: 10 20
