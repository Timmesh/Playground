# Operator Overloading Example:

# We can use the same operator for multiple purposes, which is known as operator overloading.
# Python supports operator overloading.

# Example 1: + operator can be used for Arithmetic addition and String concatenation
print(10 + 20)  # Arithmetic addition: 30
print('durga' + 'soft')  # String concatenation: durgasoft

# Operator Overloading in Custom Class:
# We can overload the + operator to work with Book objects. Python supports operator overloading.
# For every operator, magic methods are available. To overload any operator, we need to
# override the corresponding magic method in our class.

class Book:
    def __init__(self, pages):
        self.pages = pages

    # Overloading the + operator using the __add__() magic method
    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)
print('The Total Number of Pages:', b1 + b2)  # Adding pages using operator overloading

# List of operators and corresponding magic methods:
# +, -, *, /, //, %, **, +=, -=, *=, /=, //=, %=, **=, <, <=, >, >=, ==, !=
# For example, object.__add__(self, other) overloads the + operator.

# Note: For each operator, there is a corresponding magic method that can be overridden to achieve operator overloading.
