# Bitwise Operators: &, |, ^, ~, <<, >>

# Bitwise operators perform operations on individual bits of integers.
# These operators are applicable only for int and boolean types.
# If we try to apply them to any other type, we will get an error.

# Example:
print(4 & 5)  # 4 (Binary 4: 0100, Binary 5: 0101, Bitwise AND: 0100 -> Decimal 4)
print(True & True)  # True (True is treated as 1, Bitwise AND of 1 and 1 is 1)
# print(10.5 & 5.6)  # TypeError: unsupported operand type(s) for &: 'float' and 'float'

# Operator | Description
# ------- | --------
# &       | If both bits are 1, the result is 1; otherwise, the result is 0
# |       | If at least one bit is 1, the result is 1; otherwise, the result is 0
# ^       | If bits are different, the result is 1; otherwise, the result is 0
# ~       | Bitwise complement operator; 1 becomes 0, and 0 becomes 1
# <<      | Bitwise Left shift Operator
# >>      | Bitwise Right shift Operator

# Bitwise Complement Operator (~):
# We have to apply the complement to all bits, and the result is the negative value of the complement.

print(~5)  # -6 (Binary 5: 0000 0000 0000 0000 0000 0000 0000 0101, Bitwise NOT: 1111 1111 1111 1111 1111 1111 1111 1010 -> Decimal -6)
print(~-4)  # 3 (Binary -4: 1111 1111 1111 1111 1111 1111 1111 1100, Bitwise NOT: 0000 0000 0000 0000 0000 0000 0000 0011 -> Decimal 3)

# Left Shift Operator (<<):
# After shifting the empty cells, we fill them with zeros.

print(10 << 2)  # 40 (Binary 10: 0000 0000 0000 0000 0000 0000 0000 1010, Left Shift 2: 0000 0000 0000 0000 0000 0000 0010 1000 -> Decimal 40)

# Right Shift Operator (>>):
# After shifting the empty cells, we fill them with the sign bit (0 for positive and 1 for negative).

print(10 >> 2)  # 2 (Binary 10: 0000 0000 0000 0000 0000 0000 0000 1010, Right Shift 2: 0000 0000 0000 0000 0000 0000 0000 0010 -> Decimal 2)

# Bitwise operators can also be applied to boolean types.
# True is treated as 1, and False is treated as 0.

print(True & False)  # False (Bitwise AND of 1 and 0 is 0)
print(True | False)  # True (Bitwise OR of 1 and 0 is 1)
print(True ^ False)  # True (Bitwise XOR of 1 and 0 is 1)
print(~True)  # -2 (Bitwise NOT of True (1) is -2)
print(True << 2)  # 4 (Bitwise left shift of True (1) by 2 positions is 4)
print(True >> 2)  # 0 (Bitwise right shift of True (1) by 2 positions is 0)
