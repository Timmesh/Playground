# Creating a complex number with real and imaginary parts
a = 3 + 5j
print(a)  # Output: (3+5j)

# Creating another complex number with real and imaginary parts
a = 10 + 5.5j
print(a)  # Output: (10+5.5j)

# Creating a third complex number with real and imaginary parts
a = 0.5 + 0.1j
print(a)  # Output: (0.5+0.1j)

# Combining an integer in binary form with a complex number
a = 0B11 + 5j
print(a)  # Output: (3+5j)

# Trying to use binary representation for the imaginary part (results in a SyntaxError)
# a = 3 + 0B11j  # SyntaxError: invalid syntax

# Retrieving the real and imaginary parts of a complex number using built-in attributes
c = 10.5 + 3.6j
print(c.real)  # Output: 10.5
print(c.imag)  # Output: 3.6

# Performing operations on complex numbers
a = 10 + 1.5j
b = 20 + 2.5j
c = a + b
print(c)  # Output: (30+4j)
