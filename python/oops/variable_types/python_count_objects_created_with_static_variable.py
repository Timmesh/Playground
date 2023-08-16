# Program to track the Number of Objects created for a Class:

class Test:
    count = 0  # Class variable to track the number of objects

    def __init__(self):
        Test.count += 1

    @classmethod
    def noOfObjects(cls):
        print('The number of objects created for Test class:', cls.count)

# Creating objects of the Test class
t1 = Test()
t2 = Test()

# Calling the class method to display the number of objects created so far
Test.noOfObjects()

t3 = Test()
t4 = Test()
t5 = Test()

# Calling the class method again to display the updated number of objects
Test.noOfObjects()
