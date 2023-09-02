# Changing the Value of Static Variable using self or Object Reference Variable:

# If we change the value of a static variable using either self or object reference variable,
# the value of the static variable won't be changed, instead a new instance variable with the same name will be created.

class Test:
    a = 10

    def m1(self):
        self.b = 888  # Changing instance variable a using self

t1 = Test()
t1.m1()
t1.a = 33
Test.a = 22
print(Test.a)  # Original static variable value: 10
print(t1.a)    # Modified instance variable value: 888
