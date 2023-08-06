# How to Update Dictionaries:

# To update or add entries to a dictionary, we can use the square bracket notation.
# If the key is already present in the dictionary, its corresponding value will be updated with the new value.
# If the key is not present, a new entry will be added to the dictionary with the specified key-value pair.

# Example:

d = {100: "durga", 200: "ravi", 300: "shiva"}

# Initially, the dictionary contains {100: 'durga', 200: 'ravi', 300: 'shiva'}
# Let's update the value of key 400 to 'pavan'.
d[400] = "pavan"

# After the update, the dictionary becomes {100: 'durga', 200: 'ravi', 300: 'shiva', 400: 'pavan'}
print(d)

# Now, let's update the value of key 100 to 'sunny'.
d[100] = "sunny"

# After the second update, the dictionary becomes {100: 'sunny', 200: 'ravi', 300: 'shiva', 400: 'pavan'}
print(d)

# The 'd' dictionary is updated with the new key-value pairs, and the existing key-value pair for key 100 is replaced with the new value 'sunny'.
