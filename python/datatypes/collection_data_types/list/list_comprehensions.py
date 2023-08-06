# List Comprehensions

# List comprehensions provide an easy and compact way to create new lists based on some condition from any iterable object (like List, Tuple, Dictionary, Range, etc.).

# Syntax: list = [expression for item in iterable if condition]

# Example 1: Creating a list of squares of numbers from 1 to 10
s = [x*x for x in range(1, 11)]
print(s)    # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Example 2: Creating a list of powers of 2 from 1 to 5
v = [2**x for x in range(1, 6)]
print(v)    # Output: [2, 4, 8, 16, 32]

# Example 3: Creating a list of even numbers from the list 's'
m = [x for x in s if x % 2 == 0]
print(m)    # Output: [4, 16, 36, 64, 100]

# Example 4: Extracting the first character of each word from a list of words
words = ["Balaiah", "Nag", "Venkatesh", "Chiranjeevi"]
l = [w[0] for w in words]
print(l)    # Output: ['B', 'N', 'V', 'C']

# Example 5: Creating a list of numbers present in 'num1' but not in 'num2'
num1 = [10, 20, 30, 40]
num2 = [30, 40, 50, 60]
num3 = [i for i in num1 if i not in num2]
print(num3)  # Output: [10, 20]
