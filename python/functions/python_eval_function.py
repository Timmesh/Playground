# The eval() function in Python is used to evaluate a string as a Python expression.
# It takes a string as input and returns the result of the expression after evaluating it.

# Example 1: Evaluating a simple arithmetic expression
# The eval() function can evaluate arithmetic expressions and return the result.
# Let's evaluate the expression "10+20+30".

x = eval("10+20+30")
print(x)  # Output: 60

# Example 2: Evaluating an expression provided by the user
# We can use the input() function to take an expression as input from the user and then use eval() to evaluate it.
# Let's take an expression as input and evaluate it.

expression = input("Enter Expression: ")
result = eval(expression)
print(result)

# Example 3: Evaluating the input to a list, tuple, set, etc.
# The eval() function can also evaluate the input to create a list, tuple, set, etc.
# Let's take a list as input and evaluate it using eval().

input_list = "[1, 2, 3, 4, 5]"
output_list = eval(input_list)
print(output_list)  # Output: [1, 2, 3, 4, 5]


