# Finding the Number of References of an Object

# In Python, the sys module provides the getrefcount() function to find the number of references of an object.

import sys

class Test:
    pass

t1 = Test()
t2 = t1
t3 = t1
t4 = t1

# The sys.getrefcount() function returns the count of references to the given object.
# Here, the initial count is 1 (the self-reference) plus the additional references assigned to t2, t3, and t4.
print(sys.getrefcount(t1))  # 5
