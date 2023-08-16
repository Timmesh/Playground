# Positional Arguments
def sub(a, b):
    print(a - b)


sub(100, 200)  # Output: -100
sub(200, 100)  # Output: 100


# Keyword Arguments
def wish(name, msg):
    print("Hello", name, msg)


wish(name="Durga", msg="Good Morning")  # Output: Hello Durga Good Morning
wish(msg="Good Morning", name="Durga")  # Output: Hello Durga Good Morning


# Keyword and Positional Arguments Combined
def wish(name, msg):
    print("Hello", name, msg)


wish("Durga", "GoodMorning")  # Valid
wish("Durga", msg="GoodMorning")  # Valid


# wish(name="Durga", "GoodMorning")  # Invalid SyntaxError: positional argument follows keyword argument


# Default Arguments
def wish(name="Guest"):
    print("Hello", name, "Good Morning")


wish("Durga")  # Output: Hello Durga Good Morning
wish()  # Output: Hello Guest Good Morning


# Mixing Default and Non-Default Arguments
# def wish(name="Guest", msg="Good Morning"):  # Valid
# def wish(name, msg="Good Morning"):  # Valid

# def wish(name="Guest", msg):  # Invalid SyntaxError: non-default argument follows default argument


# Variable Length Arguments
def sum(*n):
    total = 0
    for n1 in n:
        total = total + n1
    print("The Sum =", total)


sum()  # Output: The Sum = 0
sum(10)  # Output: The Sum = 10
sum(10, 20)  # Output: The Sum = 30
sum(10, 20, 30, 40)  # Output: The Sum = 100


# Mixing Variable Length and Positional Arguments
def f1(n1, *s):
    print(n1)
    for s1 in s:
        print(s1)


f1(10)  # Output: 10
f1(10, 20, 30, 40)  # Output: 10 \n 20 \n 30 \n 40
f1(10, "A", 30, "B")  # Output: 10 \n A \n 30 \n B


# Using Keyword Arguments After Variable Length Arguments
def f1(*s, n1):
    for s1 in s:
        print(s1)
    print(n1)


f1("A", "B", n1=10)  # Output: A \n B \n 10
f1("A", "B", 10)  # Invalid TypeError: f1() missing 1 required keyword-only argument: 'n1'


# Keyword Variable Length Arguments
def display(**kwargs):
    for k, v in kwargs.items():
        print(k, "=", v)


display(n1=10, n2=20, n3=30)  # Output: n1 = 10 \n n2 = 20 \n n3 = 30
display(rno=100, name="Durga", marks=70,
        subject="Java")  # Output: rno = 100 \n name = Durga \n marks = 70 \n subject = Java
