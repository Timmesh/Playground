# dict Data Type:

# In Python, the dictionary data type is used to represent a collection of key-value pairs.
# Each entry in the dictionary is an item that contains a key and its associated value.

# We can create a dictionary using curly braces {} and specifying the key-value pairs separated by colons.

d = {101: 'Nakul', 102: 'Timmesh', 103: 'Pallavi'}

# This dictionary 'd' contains three key-value pairs, with keys 101, 102, and 103, and their respective values as 'Nakul', 'Timmesh', and 'Pallavi'.

# To access values from the dictionary, we can use the keys as the index.

print(d[101])  # Output: 'Nakul'
print(d[102])  # Output: 'Timmesh'
print(d[103])  # Output: 'Pallavi'

# If we try to access a key that is not present in the dictionary, it will raise a KeyError.

# d[104]  # KeyError: 104

# To add new key-value pairs or update existing ones, we can simply use the key as the index and assign a value.

d[101] = 'Naku'

# Here, the value associated with the key 101 is updated from 'Nakul' to 'Naku'.

# When we add a new key-value pair, it will be inserted into the dictionary.

d['a'] = 'apple'
d['b'] = 'banana'

print(d)  # Output: {101: 'Naku', 102: 'Timmesh', 103: 'Pallavi', 'a': 'apple', 'b': 'banana'}

# The dictionary 'd' now contains two more key-value pairs: 'a': 'apple' and 'b': 'banana'.
# The order of items in the dictionary is not guaranteed, as dictionaries are unordered collections in Python.
