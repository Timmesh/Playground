# Using Mathematical Operators for List Objects:

# Concatenation Operator (+):
# We can use the + operator to concatenate two or more lists.
a = [10, 20, 30]
b = [40, 50, 60]
c = a + b
print(c)  # Output: [10, 20, 30, 40, 50, 60]

# To use the + operator, both arguments should be list objects, otherwise we will get a TypeError.
#c = a + 40  # TypeError: can only concatenate list (not "int") to list.
c = a + [40]  # Valid, here [40] is a list containing a single element.

# Repetition Operator (*):
# We can use the * operator to repeat elements of a list a specified number of times.
x = [10, 20, 30]
y = x * 3
print(y)  # Output: [10, 20, 30, 10, 20, 30, 10, 20, 30]
