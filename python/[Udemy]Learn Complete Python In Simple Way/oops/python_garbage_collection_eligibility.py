# Garbage Collection Eligibility and Object Destruction

# If the object does not contain any reference variable, then it becomes eligible for garbage collection.
# In other words, if the reference count of an object becomes zero, the object is eligible for garbage collection.

import time

# Example 1: Demonstrating object destruction based on reference count

class Test:
    def __init__(self):
        print("Constructor Execution...")

    def __del__(self):
        print("Destructor Execution...")

t1 = Test()
t2 = t1
t3 = t2

del t1
time.sleep(5)
print("Object not yet destroyed after deleting t1")

del t2
time.sleep(5)
print("Object not yet destroyed even after deleting t2")
print("I am trying to delete the last reference variable...")

del t3

# Example 2: Demonstrating object destruction based on reference count in a list

class Test:
    def __init__(self):
        print("Constructor Execution...")

    def __del__(self):
        print("Destructor Execution...")

list_of_objects = [Test(), Test(), Test()]
del list_of_objects
time.sleep(5)
print("End of application")
