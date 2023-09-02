# Working with random Module:

# The random module in Python provides several functions for generating random numbers. These functions are commonly used in applications like game development, cryptography, and generating random numbers for authentication.

# 1. random() Function:
# The random() function generates a random float value between 0 and 1 (not inclusive).
from random import *
for i in range(10):
    print(random())

# 2. randint() Function:
# The randint() function generates a random integer between two given numbers (inclusive).
for i in range(10):
    print(randint(1, 100))  # generates a random integer between 1 and 100 (inclusive)

# 3. uniform() Function:
# The uniform() function returns random float values between two given numbers (not inclusive).
for i in range(10):
    print(uniform(1, 10))

# 4. randrange() Function:
# The randrange() function returns a random number from a specified range.
# The start argument is optional and its default value is 0.
# The step argument is optional and its default value is 1.
# The function generates a random number x such that start <= x < stop.
# It is commonly used with a single argument to generate a random number up to that limit.
for i in range(10):
    print(randrange(10))  # generates a number from 0 to 9

for i in range(10):
    print(randrange(1, 11))  # generates a number from 1 to 10

for i in range(10):
    print(randrange(1, 11, 2))  # generates a number from 1, 3, 5, 7, 9

# 5. choice() Function:
# The choice() function returns a random element from the given list or tuple.
names = ["Sunny", "Bunny", "Chinny", "Vinny", "Pinny"]
for i in range(3):
    print(choice(names))
