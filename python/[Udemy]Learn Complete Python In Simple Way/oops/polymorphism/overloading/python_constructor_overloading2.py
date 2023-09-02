# Constructor with Default Arguments in Python

# Class Test with a constructor that accepts 0, 1, 2, or 3 arguments
class Test:
    def __init__(self, a=None, b=None, c=None):
        print('Constructor with 0|1|2|3 number of arguments')

# Creating objects of the Test class with different numbers of arguments
t1 = Test()        # Output: Constructor with 0|1|2|3 number of arguments
t2 = Test(10)      # Output: Constructor with 0|1|2|3 number of arguments
t3 = Test(10, 20)  # Output: Constructor with 0|1|2|3 number of arguments
t4 = Test(10, 20, 30)  # Output: Constructor with 0|1|2|3 number of arguments
