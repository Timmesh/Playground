# The Special Variable __name__:

# In Python, every program has a special variable called __name__ that provides information about how the program is being executed.

# For standalone program execution:
def f1():
    if __name__ == '__main__':
        print("The code is executed as a standalone program")
    else:
        print("The code is executed as a module from some other program")

f1()