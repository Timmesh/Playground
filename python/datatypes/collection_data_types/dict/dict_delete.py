# How to Delete Elements from Dictionary:

# We can use different methods to delete elements from a dictionary.

# 1. del d[key]:
# The 'del' statement is used to delete an entry associated with the specified key from the dictionary.
# If the key is not available in the dictionary, a KeyError will be raised.

d = {100: "durga", 200: "ravi", 300: "shiva"}
print(d) # {100: 'durga', 200: 'ravi', 300: 'shiva'}

# Let's delete the entry with key 100.
del d[100]
print(d) # {200: 'ravi', 300: 'shiva'}

# Trying to delete a key that does not exist will raise a KeyError.
# For example, del d[400] will raise KeyError: 400 as 400 is not a key in the dictionary.

# 2. d.clear():
# The 'clear()' method is used to remove all entries from the dictionary, making it empty.

d = {100: "durga", 200: "ravi", 300: "shiva"}
print(d) # {100: 'durga', 200: 'ravi', 300: 'shiva'}

# Let's clear the dictionary.
d.clear()
print(d) # {}

# 3. del d:
# The 'del' statement can also be used to delete the entire dictionary, so we cannot access it anymore.

d = {100: "durga", 200: "ravi", 300: "shiva"}
print(d) # {100: 'durga', 200: 'ravi', 300: 'shiva'}

# Let's delete the dictionary itself.
del d
print(d) # NameError: name 'd' is not defined

# After the dictionary is deleted, trying to access it will raise a NameError.
