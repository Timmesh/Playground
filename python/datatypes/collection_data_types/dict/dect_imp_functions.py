# Important Functions of Dictionary:

# 1. dict():
# To create a dictionary, we can use the dict() constructor in three different ways:
# - To create an empty dictionary.
# - To create a dictionary with specified elements.
# - To create a dictionary from a list of tuples representing key-value pairs.

d = dict() # Creates an empty dictionary.
d = dict({100: "durga", 200: "ravi"}) # Creates a dictionary with specified elements.
d = dict([(100, "durga"), (200, "shiva"), (300, "ravi")]) # Creates a dictionary from the given list of tuples.

# 2. len():
# The len() function returns the number of items in the dictionary.

# 3. clear():
# The clear() method removes all elements from the dictionary, making it empty.

# 4. get():
# The get() method is used to get the value associated with a key. It returns the corresponding value if the key is
# available, otherwise it returns None (or a specified default value) without raising any error.

d = {100: "durga", 200: "ravi", 300: "shiva"}
print(d.get(100)) # 'durga'
print(d.get(400)) # None
print(d.get(100, "Guest")) # 'durga'
print(d.get(400, "Guest")) # 'Guest'

# 5. pop():
# The pop() method removes the entry associated with the specified key and returns the corresponding value. If the
# specified key is not available, it will raise a KeyError.

d = {100: "durga", 200: "ravi", 300: "shiva"}
print(d.pop(100)) # 'durga'
print(d) # {200: 'ravi', 300: 'shiva'}
# print(d.pop(400)) # KeyError: 400

# 6. popitem():
# The popitem() method removes an arbitrary item (key-value pair) from the dictionary and returns it. If the dictionary
# is empty, it will raise a KeyError.

d = {100: "durga", 200: "ravi", 300: "shiva"}
print(d.popitem()) # (300, 'shiva')
print(d) # {100: 'durga', 200: 'ravi'}
# print(d.popitem()) # KeyError: 'popitem(): dictionary is empty'

# 7. keys():
# The keys() method returns a view of all keys associated with the dictionary.

d = {100: "durga", 200: "ravi", 300: "shiva"}
print(d.keys()) # dict_keys([100, 200, 300])
for k in d.keys():
    print(k, end=' ') # 100 200 300

# 8. values():
# The values() method returns a view of all values associated with the dictionary.

d = {100: "durga", 200: "ravi", 300: "shiva"}
print(d.values()) # dict_values(['durga', 'ravi', 'shiva'])
for v in d.values():
    print(v, end=' ') # durga ravi shiva

# 9. items():
# The items() method returns a view of all key-value pairs in the dictionary as tuples [(k, v), (k, v), (k, v)].

d = {100: "durga", 200: "ravi", 300: "shiva"}
for k, v in d.items():
    print(k, "--", v, end=' ') # 100 -- durga 200 -- ravi 300 -- shiva

# 10. copy():
# The copy() method is used to create an exactly duplicate dictionary (a cloned copy).

d1 = d.copy()

# 11. setdefault():
# The setdefault() method is used to get the value associated with a key. If the key is not available, it adds the
# specified key-value as a new item to the dictionary.

d = {100: "durga", 200: "ravi", 300: "shiva"}
print(d.setdefault(400, "pavan")) # 'pavan'
print(d) # {100: 'durga', 200: 'ravi', 300: 'shiva', 400: 'pavan'}
print(d.setdefault(100, "sachin")) # 'durga'
print(d) # {100: 'durga', 200: 'ravi', 300: 'shiva', 400: 'pavan'}

# 12. update():
# The update() method is used to add all items present in the dictionary x to the dictionary d.

d = {100: "durga", 200: "ravi"}
x = {300: "shiva", 400: "pavan"}
d.update(x)
print(d) # {100: 'durga', 200: 'ravi', 300: 'shiva', 400: 'pavan'}
