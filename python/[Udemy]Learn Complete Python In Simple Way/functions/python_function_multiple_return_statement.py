# Function to return the sum and subtraction of two numbers
def sum_sub(a, b):
    sum_val = a + b
    sub_val = a - b
    return sum_val, sub_val

# Calling the 'sum_sub' function and unpacking the returned values
x, y = sum_sub(100, 50)
print("The Sum is:", x)  # Output: The Sum is: 150
print("The Subtraction is:", y)  # Output: The Subtraction is: 50

# Function to return the sum, subtraction, multiplication, and division of two numbers
def calc(a, b):
    sum_val = a + b
    sub_val = a - b
    mul_val = a * b
    div_val = a / b
    return sum_val, sub_val, mul_val, div_val

# Calling the 'calc' function and storing the returned tuple in 't'
t = calc(100, 50)
print("The Results are:")
for i in t:
    print(i)
