# Define class A with a method m1
class A:
    def m1(self):
        print('A class Method')

# Define class B with a method m1
class B:
    def m1(self):
        print('B class Method')

# Define class C with a method m1
class C:
    def m1(self):
        print('C class Method')

# Define class X inheriting from classes A and B, with a method m1
class X(A, B):
    def m1(self):
        print('X class Method')

# Define class Y inheriting from classes B and C, with a method m1
class Y(B, C):
    def m1(self):
        print('Y class Method')

# Define class P inheriting from classes X, Y, and C, with a method m1
class P(X, Y, C):
    def m1(self):
        print('P class Method')

# Finding MRO for class P using C3 Algorithm:
# MRO(X) = X + Merge(MRO(P1), MRO(P2), ..., ParentList)
# MRO(P) = P + Merge(MRO(X), MRO(Y), MRO(C), XYC)
#        = P + Merge(XABO, YBCO, CO, XYC)
#        = P + X + Merge(ABO, YBCO, CO, YC)
#        = P + X + A + Merge(BO, YBCO, CO, YC)
#        = P + X + A + Y + Merge(BO, BCO, CO, C)
#        = P + X + A + Y + B + Merge(O, CO, CO, C)
#        = P + X + A + Y + B + C + Merge(O, O, O)
#        = P + X + A + Y + B + C + O

# Create an instance of class P
p = P()
print(P.mro());
# Call the method m1 on the instance of class P
p.m1()
