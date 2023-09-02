# Define the class A
class A:
    def m1(self):
        print('A class Method')

# Define the class B inheriting from class A
class B(A):
    def m1(self):
        print('B class Method')

# Define the class C inheriting from class B
class C(B):
    def m1(self):
        print('C class Method')

# Define the class D inheriting from class C
class D(C):
    def m1(self):
        print('D class Method')

# Define the class E inheriting from class D
class E(D):
    def m1(self):
        # Calling the m1() method of class A using A.m1(self)
        A.m1(self)
        # Calling the m1() method of superclass C using super()
        super(C, self).m1()


# Create an instance of class E
e = E()
# Call the m1() method of class E, which will call the m1() method of class A
e.m1()
