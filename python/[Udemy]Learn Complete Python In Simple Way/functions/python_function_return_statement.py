# Function to return the sum of two numbers
def add(x, y):
    return x + y

# Calling the 'add' function and printing the result
result = add(10, 20)
print("The sum is", result)  # Output: The sum is 30

# Function without return statement (default return value is None)
def f1():
    print("Hello")

f1()           # Output: Hello
print(f1())    # Output: Hello \n None (due to the print inside the function)

# Function to check whether a number is Even or Odd
def even_odd(num):
    if num % 2 == 0:
        print(num, "is Even Number")
    else:
        print(num, "is Odd Number")

even_odd(10)  # Output: 10 is Even Number
even_odd(15)  # Output: 15 is Odd Number

# Function to find the factorial of a given number
def fact(num):
    result = 1
    while num >= 1:
        result = result * num
        num = num - 1
    return result

# Finding and printing factorial for numbers from 1 to 4
for i in range(1, 5):
    print("The Factorial of", i, "is:", fact(i))
