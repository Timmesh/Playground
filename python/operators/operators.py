# OPERATORS

# Operators are symbols in Python that perform specific operations on operands.

# 1) Arithmetic Operators:
# These operators are used to perform arithmetic operations like addition, subtraction, multiplication, division, etc.

# Example:
a = 10
b = 5

addition_result = a + b
subtraction_result = a - b
multiplication_result = a * b
division_result = a / b
remainder_result = a % b
exponentiation_result = a ** b
floor_division_result = a // b

print(f"Addition: {addition_result}")  # Addition: 15
print(f"Subtraction: {subtraction_result}")  # Subtraction: 5
print(f"Multiplication: {multiplication_result}")  # Multiplication: 50
print(f"Division: {division_result}")  # Division: 2.0
print(f"Remainder: {remainder_result}")  # Remainder: 0
print(f"Exponentiation: {exponentiation_result}")  # Exponentiation: 100000
print(f"Floor Division: {floor_division_result}")  # Floor Division: 2

# 2) Relational Operators (or Comparison Operators):
# These operators are used to compare two values or operands.

# Example:
x = 10
y = 20

greater_than_result = x > y
less_than_result = x < y
greater_than_or_equal_result = x >= y
less_than_or_equal_result = x <= y
equality_result = x == y
inequality_result = x != y

print(f"Greater Than: {greater_than_result}")  # Greater Than: False
print(f"Less Than: {less_than_result}")  # Less Than: True
print(f"Greater Than or Equal: {greater_than_or_equal_result}")  # Greater Than or Equal: False
print(f"Less Than or Equal: {less_than_or_equal_result}")  # Less Than or Equal: True
print(f"Equality: {equality_result}")  # Equality: False
print(f"Inequality: {inequality_result}")  # Inequality: True

# 3) Logical Operators:
# These operators are used to perform logical operations like AND, OR, NOT.

# Example:
p = True
q = False

and_result = p and q
or_result = p or q
not_result = not p

print(f"AND: {and_result}")  # AND: False
print(f"OR: {or_result}")  # OR: True
print(f"NOT: {not_result}")  # NOT: False

# 4) Bitwise Operators:
# These operators are used to perform bitwise operations on binary numbers.

# Example:
a = 10  # Binary: 1010
b = 5   # Binary: 0101

bitwise_and_result = a & b   # Binary AND: 0000 (Decimal: 0)
bitwise_or_result = a | b    # Binary OR: 1111 (Decimal: 15)
bitwise_xor_result = a ^ b   # Binary XOR: 1111 (Decimal: 15)
bitwise_complement_a = ~a    # Binary NOT: 11111111111111111111111111110101 (Decimal: -11)
left_shift_result = a << 2   # Binary Left Shift: 101000 (Decimal: 40)
right_shift_result = a >> 2  # Binary Right Shift: 10 (Decimal: 2)

print(f"Bitwise AND: {bitwise_and_result}")  # Bitwise AND: 0
print(f"Bitwise OR: {bitwise_or_result}")    # Bitwise OR: 15
print(f"Bitwise XOR: {bitwise_xor_result}")  # Bitwise XOR: 15
print(f"Bitwise NOT A: {bitwise_complement_a}")  # Bitwise NOT A: -11
print(f"Left Shift: {left_shift_result}")   # Left Shift: 40
print(f"Right Shift: {right_shift_result}")  # Right Shift: 2

# 5) Assignment Operators:
# These operators are used to assign values to variables.

# Example:
x = 10
y = 5

x += y  # Equivalent to x = x + y
print(f"x after addition assignment: {x}")  # x after addition assignment: 15

x -= y  # Equivalent to x = x - y
print(f"x after subtraction assignment: {x}")  # x after subtraction assignment: 10

x *= y  # Equivalent to x = x * y
print(f"x after multiplication assignment: {x}")  # x after multiplication assignment: 50

x /= y  # Equivalent to x = x / y
print(f"x after division assignment: {x}")  # x after division assignment: 10.0

# 6) Special Operators:
# There are two special operators: Identity Operator (is, is not) and Membership Operator (in, not in).

# Identity Operator:
# The 'is' operator is used to check if two variables point to the same object in memory.
# The 'is not' operator is used to check if two variables do not point to the same object.

# Example:
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, as a and b both refer to the same list object in memory.
print(a is c)  # False, as a and c are two different list objects with the same values.

# Membership Operator:
# The 'in' operator is used to check if a value is present in a sequence (e.g., string, list, tuple, set, dictionary keys).
# The 'not in' operator is used to check if a value is not present in a sequence.

# Example:
name = "John"
names_list = ["Alice", "Bob", "John", "Mike"]

print(name in names_list)     # True, as "John" is present in the list.
print(name not in names_list) # False, as "John" is present in the list.

# These are the basic operators available in Python that allow performing various operations on different types of data.
# Understanding and using these operators is fundamental in Python programming.
