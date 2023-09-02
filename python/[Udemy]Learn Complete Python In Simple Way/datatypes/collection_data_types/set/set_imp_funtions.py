# Important Functions of Set:

# 1. add(x): Adds item x to the set.
s = {10, 20, 30}
s.add(40)
print(s)  # {40, 10, 20, 30}

# Explanation:
# We used the add() function to add the item 40 to the set s.

# 2. update(x, y, z): To add multiple items to the set.
s = {10, 20, 30}
l = [40, 50, 60, 10]
s.update(l, range(5))
print(s)  # {0, 1, 2, 3, 4, 40, 10, 50, 20, 60, 30}

# Explanation:
# We used the update() function to add multiple items to the set s.
# The items from list l and the range from 0 to 4 were added to the set s.

# 3. copy(): Returns a copy of the set.
s = {10, 20, 30}
s1 = s.copy()
print(s1)

# Explanation:
# We used the copy() function to create a copy of the set s and stored it in s1.

# 4. pop(): It removes and returns some random element from the set.
s = {40, 10, 30, 20}
print(s)  # {40, 10, 20, 30}
print(s.pop())  # 40
print(s)  # {10, 20, 30}

# Explanation:
# We used the pop() function to remove and return a random element from the set s.

# 5. remove(x): It removes the specified element from the set.
s = {40, 10, 30, 20}
s.remove(30)
print(s)  # {40, 10, 20}

# Explanation:
# We used the remove() function to remove the element 30 from the set s.

# 6. discard(x): It removes the specified element from the set.
s = {10, 20, 30}
s.discard(10)
print(s)  # {20, 30}
s.discard(50)
print(s)  # {20, 30}

# Explanation:
# We used the discard() function to remove the element 10 from the set s. If the element is not present, no error is raised.

# 7. clear(): To remove all elements from the Set.
s = {10, 20, 30}
print(s)  # {10, 20, 30}
s.clear()
print(s)  # set()

# Explanation:
# We used the clear() function to remove all elements from the set s, making it an empty set.
