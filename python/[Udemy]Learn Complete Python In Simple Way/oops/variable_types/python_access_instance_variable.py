# How to Access Instance Variables:
# We can access instance variables within the class by using the self variable and outside of the class by using object reference.

class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def display(self):
        print(self.a)
        print(self.b)

t = Test()
t.display()  # 10 20
print(t.a, t.b)  # 10 20
