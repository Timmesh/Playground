# How to Create Dictionary:

# 1. We can create an empty dictionary by using curly braces {}.

d = {}

# This creates an empty dictionary 'd' with no key-value pairs.

# 2. We can add key-value pairs to the dictionary as follows:

d[100] = "durga"
d[200] = "ravi"
d[300] = "shiva"

# Here, we have added three key-value pairs to the dictionary 'd'.

# The keys are 100, 200, and 300, and their respective values are 'durga', 'ravi', and 'shiva'.

# After adding these key-value pairs, the dictionary 'd' will be:

print(d)  # Output: {100: 'durga', 200: 'ravi', 300: 'shiva'}

# 3. If we know the data in advance, we can directly create the dictionary with key-value pairs.

d = {100: 'durga', 200: 'ravi', 300: 'shiva'}

# Here, we are directly creating the dictionary 'd' with the specified key-value pairs.

# The dictionary 'd' will have the same content as before.

# 4. Another way to create a dictionary is by using the dict() constructor.

# We can pass a list of key-value tuples to the dict() constructor to create the dictionary.

d = dict([(100, 'durga'), (200, 'ravi'), (300, 'shiva')])

# This will create the same dictionary 'd' with the specified key-value pairs.

# In this example, we passed a list of tuples to the dict() constructor,
# where each tuple contains a key and its associated value.

# The dictionary 'd' will have the same content as before:

print(d)  # Output: {100: 'durga', 200: 'ravi', 300: 'shiva'}
