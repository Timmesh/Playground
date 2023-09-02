# Manipulating Elements of List:

# append() Function: We can use append() function to add an item at the end of the list.
list = []
list.append("A")
list.append("B")
list.append("C")
print(list)  # Output: ['A', 'B', 'C']

# To add all elements to the list up to 100 which are divisible by 10
list = []
for i in range(101):
    if i % 10 == 0:
        list.append(i)
print(list)  # Output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# insert() Function: To insert an item at the specified index position
# If the specified index is greater than the max index, then the element will be inserted at the last position.
# If the specified index is smaller than the min index, then the element will be inserted at the first position.
n = [1, 2, 3, 4, 5]
n.insert(1, 888)
print(n)  # Output: [1, 888, 2, 3, 4, 5]

n = [1, 2, 3, 4, 5]
n.insert(10, 777)
n.insert(-10, 999)
print(n)  # Output: [999, 1, 2, 3, 4, 5, 777]

# extend() Function: To add all items of one list to another
order1 = ["Chicken", "Mutton", "Fish"]
order2 = ["RC", "KF", "FO"]
order1.extend(order2)
print(order1)  # Output: ['Chicken', 'Mutton', 'Fish', 'RC', 'KF', 'FO']

order = ["Chicken", "Mutton", "Fish"]
order.extend("Mushroom")
print(order)  # Output: ['Chicken', 'Mutton', 'Fish', 'M', 'u', 's', 'h', 'r', 'o', 'o', 'm']

# remove() Function: We can use this function to remove a specified item from the list.
# If the item is present multiple times, then only the first occurrence will be removed.
n = [10, 20, 10, 30]
n.remove(10)
print(n)  # Output: [20, 10, 30]

n = [10, 20, 10, 30]
n.remove(40)  # ValueError: list.remove(x): x not in list
print(n)

# pop() Function: It removes and returns the last element of the list.
n = [10, 20, 30, 40]
print(n.pop())  # Output: 40
print(n.pop())  # Output: 30
print(n)  # Output: [10, 20]

n = []
# print(n.pop())  # IndexError: pop from empty list

# pop(index) -> To remove and return the element present at the specified index.
# pop() -> To remove and return the last element of the list
n = [10, 20, 30, 40, 50, 60]
print(n.pop())  # Output: 60
print(n.pop(1))  # Output: 20
# print(n.pop(10))  # IndexError: pop index out of range
