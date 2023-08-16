# Local Variables:

# Sometimes, to meet the temporary requirements of a programmer, we can declare variables inside a method directly.
# Such type of variables are called local variables or temporary variables.
# Local variables will be created at the time of method execution and destroyed once the method completes.
# Local variables of a method cannot be accessed from outside of the method.

class Test:

    def m1(self):
        a = 1000  # 'a' is a local variable of method m1
        print(a)

    def m2(self):
        b = 2000  # 'b' is a local variable of method m2
        print(b)

t = Test()
t.m1()  # Output: 1000
t.m2()  # Output: 2000
