# Typecasting or Type Coersion is the process of converting one data type to another.

# int(): Convert values from other types to int
print(int(123.987))  # Output: 123
# print(int(10 + 5j))  # TypeError: can't convert complex to int
print(int(True))  # Output: 1
print(int(False))  # Output: 0
print(int("10"))  # Output: 10
# print(int("10.5"))  # ValueError: invalid literal for int() with base 10: '10.5'
# print(int("ten"))  # ValueError: invalid literal for int() with base 10: 'ten'
# print(int("0B1111"))  # ValueError: invalid literal for int() with base 10: '0B1111'

# float(): Convert other types to float
print(float(10))  # Output: 10.0
# print(float(10 + 5j))  # TypeError: can't convert complex to float
print(float(True))  # Output: 1.0
print(float(False))  # Output: 0.0
print(float("10"))  # Output: 10.0
print(float("10.5"))  # Output: 10.5
# print(float("ten"))  # ValueError: could not convert string to float: 'ten'
# print(float("0B1111"))  # ValueError: could not convert string to float: '0B1111'

# complex(): Convert other types to complex
# Form-1: complex(x) - Convert x into a complex number with real part x and imaginary part 0.
print(complex(10))  # Output: 10+0j
print(complex(10.5))  # Output: 10.5+0j
print(complex(True))  # Output: 1+0j
print(complex(False))  # Output: 0j
print(complex("10"))  # Output: 10+0j
print(complex("10.5"))  # Output: 10.5+0j
# print(complex("ten"))  # ValueError: complex() arg is a malformed string

# Form-2: complex(x, y) - Convert x and y into a complex number where x is the real part and y is the imaginary part.
print(complex(10, -2))  # Output: 10-2j
print(complex(True, False))  # Output: 1+0j

# bool(): Convert other types to bool
print(bool(0))  # Output: False
print(bool(1))  # Output: True
print(bool(10))  # Output: True
print(bool(10.5))  # Output: True
print(bool(0.178))  # Output: True
print(bool(0.0))  # Output: False
print(bool(10 - 2j))  # Output: True
print(bool(0 + 1.5j))  # Output: True
print(bool(0 + 0j))  # Output: False
print(bool("True"))  # Output: True
print(bool("False"))  # Output: True
print(bool(""))  # Output: False

# str(): Convert other type values to str
print(str(10))  # Output: '10'
print(str(10.5))  # Output: '10.5'
print(str(10 + 5j))  # Output: '(10+5j)'
print(str(True))  # Output: 'True'
