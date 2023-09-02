# Nested Lists

# Nested lists are lists that contain other lists as elements.

n = [10, 20, [30, 40]]
print(n)        # Output: [10, 20, [30, 40]]
print(n[0])     # Output: 10
print(n[2])     # Output: [30, 40]
print(n[2][0])  # Output: 30
print(n[2][1])  # Output: 40

# Explanation:
# The list 'n' contains elements [10, 20, [30, 40]].
# n[0] gives the first element of the list, which is 10.
# n[2] gives the third element of the list, which is [30, 40].
# n[2][0] gives the first element of the nested list, which is 30.
# n[2][1] gives the second element of the nested list, which is 40.
