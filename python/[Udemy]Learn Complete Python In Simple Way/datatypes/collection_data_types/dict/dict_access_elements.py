# How to Access Data from the Dictionary:

# 1. We can access data from the dictionary using keys.

d = {100: 'durga', 200: 'ravi', 300: 'shiva'}

# To access the value associated with a particular key, we can use the key inside square brackets.

print(d[100])  # Output: 'durga'
print(d[300])  # Output: 'shiva'

# If the specified key is not available in the dictionary, we will get a KeyError.

# 2. To prevent KeyError, we can check whether the key is present in the dictionary using the 'in' operator.

if 400 in d:
    print(d[400])
else:
    print("Key 400 not found in the dictionary.")

# This will print "Key 400 not found in the dictionary." because the key 400 is not present in the dictionary.

# Note: The 'has_key()' function is available only in Python 2 and is not available in Python 3.
# Therefore, we should use the 'in' operator for checking key existence in Python 3.

# Example of entering name and percentage marks in a dictionary and displaying information:

rec = {}
n = int(input("Enter number of students: "))
i = 1
while i <= n:
    name = input("Enter Student Name: ")
    marks = input("Enter % of Marks of Student: ")
    rec[name] = marks
    i = i + 1

print("Name of Student", "\t", "% of marks")
for name, marks in rec.items():
    print("\t", name, "\t\t", marks)

# In this program, we are entering the names and percentage marks of 'n' students and storing them in the dictionary 'rec'.
# Then, we are displaying the information using a loop and the 'items()' method, which returns key-value pairs from the dictionary.
