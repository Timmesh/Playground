# Destructors

# Explanation of Destructors in Python
# A destructor is a special method in Python with the name '__del__'.
# Just before destroying an object, the Garbage Collector always calls the destructor
# to perform clean-up activities, such as resource deallocation (e.g., closing a database connection).
# Once the destructor execution is completed, the Garbage Collector automatically destroys that object.

# Note:
# The job of the destructor is not to destroy the object; its main purpose is to perform
# clean-up activities before the object is removed from memory.

import time

class Test:
    def __init__(self):
        print("Object Initialization...")

    def __del__(self):
        print("Fulfilling Last Wish and performing clean-up activities...")

t1 = Test()   # Object Initialization...
t1 = None     # Fulfilling Last Wish and performing clean-up activities...
time.sleep(5) # Wait for 5 seconds
print("End of application")  # End of application
