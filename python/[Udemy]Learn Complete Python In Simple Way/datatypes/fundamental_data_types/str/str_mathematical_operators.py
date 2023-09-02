# Mathematical Operators for String

# Concatenation (+) Operator
s = 'nakul'

# Concatenating the first character converted to uppercase with the rest of the string
print(s[0].upper() + s[1:len(s)])  # Output: 'Nakul'

# Concatenating the first character converted to uppercase, middle characters,
# and the last character converted to uppercase
print(s[0].upper() + s[1:len(s) - 1] + s[-1].upper())  # Output: 'NakuL'

# The + Operator requires both operands to be strings. Attempting to concatenate a string with an int raises an error.
# TypeError: can only concatenate str (not "int") to str
# print(s + 10)

# Finding the length of the string (number of characters in the string)
print(len(s))  # Output: 5

# Repetition (*) Operator
print(s * 3)  # Output: 'nakulnakulnakul'
print(2 * s)  # Output: 'nakulnakul'

# Repeating the string "Nakul" twice using different syntaxes
print(2 * "Nakul")  # Output: 'NakulNakul'
print("Nakul" * 2)  # Output: 'NakulNakul'

# Attempting to multiply a string by a float raises an error
# TypeError: can't multiply sequence by non-int of type 'float'
# print(2.5 * "Nakul")

# Attempting to multiply two strings raises an error
# TypeError: can't multiply sequence by non-int of type 'str'
# print("Nakul" * "Nakul")
