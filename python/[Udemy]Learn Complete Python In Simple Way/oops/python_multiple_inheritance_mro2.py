# Define class A
class A:
    pass

# Define class B inheriting from A
class B(A):
    pass

# Define class C inheriting from A
class C(A):
    pass

# Define class D inheriting from both B and C
class D(B, C):
    pass

# Print MRO for class A
print("MRO for class A:", A.mro())  # Output: [<class '__main__.A'>, <class 'object'>]

# Print MRO for class B
print("MRO for class B:", B.mro())  # Output: [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

# Print MRO for class C
print("MRO for class C:", C.mro())  # Output: [<class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# Print MRO for class D
print("MRO for class D:", D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
