# Python String Operations and Methods Examples

# This Python script demonstrates various operations and methods related to string manipulation. It covers common string
# operations such as finding the length of a string, checking membership of characters or substrings, comparing strings,
# removing spaces, finding substrings, counting occurrences, replacing substrings, splitting strings, joining strings,
# changing case, checking starting and ending parts, and formatting strings using the format() method.

# Function 1: Length of the String
s = 'Nakul'
print(len(s))  # Output: 5

# Function 2: Checking for Substring Membership
s = 'durga'
print('d' in s)  # Output: True
print('z' in s)  # Output: False
print('z' not in s)  # Output: True

# Function 3: Checking for Substring Presence
s = input("Enter main string:")
subs = input("Enter sub string:")
if subs in s:
    print(subs, "is found in the main string")
else:
    print(subs, "is not found in the main string")

# Function 4: Comparing Strings
s1 = input("Enter first string:")
s2 = input("Enter second string:")
if s1 == s2:
    print("Both strings are equal")
elif s1 < s2:
    print("First String is less than Second String")
else:
    print("First String is greater than Second String")

# Function 5: Removing Spaces from the String
city = input("Enter your city Name:")
scity = city.strip()
if scity == 'Hyderabad':
    print("Hello Hyderbadi...Adab")
elif scity == 'Chennai':
    print("Hello Madrasi...Vanakkam")
elif scity == "Bangalore":
    print("Hello Kannadiga...Shubhodaya")
else:
    print("Your entered city is invalid")

# Function 6: Finding Substrings
# For forward direction: find() and index()
# For backward direction: rfind() and rindex()

s = "Learning Python is very easy"
print(s.find("Python"))  # Output: 9
print(s.find("Java"))  # Output: -1
print(s.find("r"))  # Output: 3
print(s.rfind("r"))  # Output: 21

# By default, find() method can search throughout the string. We can also specify the boundaries to search.
s = "durgaravipavanshiva"
print(s.find('a'))  # Output: 4
print(s.find('a', 7, 15))  # Output: 10
print(s.find('z', 7, 15))  # Output: -1

# index() method is exactly the same as find() method, except that if the specified substring is not available,
# then we will get ValueError.
s = input("Enter main string:")
subs = input("Enter sub string:")
try:
    n = s.index(subs)
except ValueError:
    print("Substring not found")
else:
    print("Substring found")

# Function 7: Counting Substrings
# We can find the number of occurrences of a substring present in the given string using the count() method.
# count() will search throughout the string by default, but we can specify the boundaries as well.

s = "abcabcabcabcadda"
print(s.count('a'))  # Output: 6
print(s.count('ab'))  # Output: 4
print(s.count('a', 3, 7))  # Output: 2

# Function 8: Replacing a String with Another String
s = "Learning Python is very difficult"
s1 = s.replace("difficult", "easy")
print(s1)  # Output: "Learning Python is very easy"

s = "ababababababab"
s1 = s.replace("a", "b")
print(s1)  # Output: "bbbbbbbbbbbbbb"

# String objects are immutable, hence with the replace() method, a new object is created, but the existing object
# won't be changed.
s = "abab"
s1 = s.replace("a", "b")
print(s, "is available at:", id(s))
print(s1, "is available at:", id(s1))

# Function 9: Splitting Strings
# The default separator is space. The return type of the split() method is a List.

s = "durga software solutions"
l = s.split()
print(l)  # Output: ['durga', 'software', 'solutions']
for x in l:
    print(x)

s = "22-02-2018"
l = s.split('-')
print(l)  # Output: ['22', '02', '2018']
for x in l:
    print(x)

# Function 10: Joining Strings
# We can join a group of strings (List OR Tuple) with the given separator.
# s = separator.join(group of strings)

t = ('sunny', 'bunny', 'chinny')
s = '-'.join(t)
print(s)  # Output: 'sunny-bunny-chinny'

l = ['hyderabad', 'singapore', 'london', 'dubai']
s = ':'.join(l)
print(s)  # Output: 'hyderabad:singapore:london:dubai'

# Function 11: Changing Case of a String
s = 'learning Python is very Easy'
print(s.upper())  # Output: 'LEARNING PYTHON IS VERY EASY'
print(s.lower())  # Output: 'learning python is very easy'
print(s.swapcase())  # Output: 'LEARNING pYTHON IS VERY eASY'
print(s.title())  # Output: 'Learning Python Is Very Easy'
print(s.capitalize())  # Output: 'Learning python is very easy'

# Function 12: Checking Starting and Ending Part of the String
s = 'learning Python is very easy'
print(s.startswith('learning'))  # Output: True
print(s.endswith('learning'))  # Output: False
print(s.endswith('easy'))  # Output: True

# Function 13: Checking Type of Characters Present in a String
print('Durga786'.isalnum())  # Output: True
print('durga786'.isalpha())  # Output: False
print('durga'.isalpha())  # Output: True
print('durga'.isdigit())  # Output: False
print('786786'.isdigit())  # Output: True
print('abc'.islower())  # Output: True
print('Abc'.islower())  # Output: False
print('abc123'.islower())  # Output: True
print('ABC'.isupper())  # Output: True
print('Learning python is Easy'.istitle())  # Output: False
print('Learning Python Is Easy'.istitle())  # Output: True
print(' '.isspace())  # Output: True

s = input("Enter any character:")
if s.isalnum():
    print("Alphanumeric Character")
    if s.isalpha():
        print("Alphabet character")
    if s.islower():
        print("Lowercase alphabet character")
    else:
        print("Uppercase alphabet character")
elif s.isdigit():
    print("It is a digit")
elif s.isspace():
    print("It is a space character")
else:
    print("Non-space Special Character")

# Function 14: Formatting Strings
name = 'Nakul'
salary = 1000000
age = 18
print("{}'s salary is {} and his age is {}".format(name, salary, age))
print("{0}'s salary is {1} and his age is {2}".format(name, salary, age))
print("{x}'s salary is {y} and his age is {z}".format(z=age, y=salary, x=name))


