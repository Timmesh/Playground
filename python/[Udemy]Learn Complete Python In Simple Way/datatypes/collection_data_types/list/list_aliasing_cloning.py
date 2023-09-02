# Aliasing and Cloning of List Objects:

# Aliasing:
# When we assign a list to another variable, both variables point to the same list object in memory.
# If we modify the list through one variable, the changes will be reflected in the other variable as well.
x = [10, 20, 30, 40]
y = x
print(id(x))  # Output: Memory address of list x
print(id(y))  # Output: Memory address of list y (same as x)

# Modifying the list through one variable will reflect the changes in the other variable.
x = [10, 20, 30, 40]
y = x
y[1] = 777
print(x)  # Output: [10, 777, 30, 40]
print(y)  # Output: [10, 777, 30, 40]

# Cloning using Slice Operator:
# Cloning means creating a new copy of the list, so that changes in one list do not affect the other.
# Using slice operator [:] creates a shallow copy of the list.
x = [10, 20, 30, 40]
y = x[:]  # Cloning the list using slice operator
y[1] = 777
print(x)  # Output: [10, 20, 30, 40]
print(y)  # Output: [10, 777, 30, 40]

# Cloning using copy() Function:
# Another way to clone a list is by using the copy() function.
# This also creates a shallow copy of the list.
x = [10, 20, 30, 40]
y = x.copy()  # Cloning the list using copy() function
y[1] = 777
print(x)  # Output: [10, 20, 30, 40]
print(y)  # Output: [10, 777, 30, 40]
