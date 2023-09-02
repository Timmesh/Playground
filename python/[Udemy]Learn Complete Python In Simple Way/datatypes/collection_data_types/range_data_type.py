# Range Data Type

# The range data type represents a sequence of numbers.
# The elements present in a range data type are not modifiable; it is immutable.

# Form-1: range(10) generates numbers from 0 to 9

r = range(10)
for i in r:
    print(i)  # 0 to 9

# Explanation:
# The range() function generates a sequence of numbers starting from 0 and stopping at (end-1),
# where 'end' is the argument passed to the range function (10 in this case).
# It includes numbers from 0 to 9, as 10 is not included in the range.

# Form-2: range(10, 20) generates numbers from 10 to 19

r = range(10, 20)
for i in r:
    print(i)  # 10 to 19

# Explanation:
# The range() function with two arguments generates a sequence of numbers starting from the first argument (10)
# and stopping at (end-1), where 'end' is the second argument (20 in this case).
# It includes numbers from 10 to 19, as 20 is not included in the range.

# Form-3: range(10, 20, 2) with 2 as the step value, generates numbers with a step of 2

r = range(10, 20, 2)
for i in r:
    print(i)  # 10, 12, 14, 16, 18

# Explanation:
# The range() function with three arguments generates a sequence of numbers starting from the first argument (10),
# stopping at (end-1) where 'end' is the second argument (20 in this case),
# and the third argument (2) specifies the step value.
# It generates numbers with a step of 2, so it includes 10, 12, 14, 16, and 18.

# Accessing elements in the range data type by index

r = range(10, 20)
r[0]  # 10
#r[15]  # IndexError: range object index out of range

# Explanation:
# Like lists and tuples, range data types support indexing, and the index starts from 0.
# r[0] gives 10, which is the first element in the range (starting from 10 and stopping at 19).
# r[15] gives an IndexError because the range object has only 10 elements, and there is no element at index 15.

# Modifying values of the range data type is not allowed

r[0] = 100
# TypeError: 'range' object does not support item assignment

# Explanation:
# Range data type is immutable, meaning its elements cannot be modified once created.
# So, trying to modify the element at index 0 (r[0]) to 100 results in a TypeError.

# Creating a list from a range data type

l = list(range(10))
print(l)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Explanation:
# The list() function is used to convert the range data type into a list.
# In this example, it generates a list of numbers from 0 to 9 using the range(10) expression.
