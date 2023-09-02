class X:
    a = 10
    def __init__(self):
        self.b = 20

    def m1(self):
        print("m1 method of X class")

class Y:
    c = 30
    def __init__(self):
        self.d = 40

    def m2(self):
        print("m2 method of Y class")

    def m3(self):
        x1 = X()
        print(x1.a)   # Accessing X's class variable
        print(x1.b)   # Accessing X's instance variable
        x1.m1()       # Accessing X's method
        print(Y.c)    # Accessing Y's class variable
        print(self.d) # Accessing Y's instance variable
        self.m2()     # Accessing Y's method
        print("m3 method of Y class")

y1 = Y()
y1.m3()
