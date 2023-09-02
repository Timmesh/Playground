# Traversing the Elements of List

# By using for Loop:
# Example 1: Traverse all elements of the list
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n1 in n:
    print(n1)

# Example 2: Traverse and print only even elements from the list
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n1 in n:
    if n1 % 2 == 0:
        print(n1)

# By using while Loop:
# Example 3: Traverse all elements of the list using a while loop
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(n):
    print(n[i], end=' ')
    i = i + 1
print()
# To display Elements by Index wise:
# Example 4: Traverse the list and display elements with their index
l = ["A", "B", "C"]
x = len(l)
for i in range(x):
    print(l[i], "is available at positive index:", i, "and at negative index:", i - x)
