## Anonymous Functions (Lambda Functions)
# Sometimes we can declare a function without any name; such type of nameless functions are called anonymous functions or lambda functions.

# Normal Function to Calculate Square
def squareIt(n):
    """
    Calculate the square of a number using a normal function.

    Args:
        n (int): The input number

    Returns:
        int: The square of the input number
    """
    return n * n

# Lambda Function to Calculate Square
square_lambda = lambda n: n * n

# Example Usage:
num = 5
print("Square of", num, "using normal function:", squareIt(num))
# Output: Square of 5 using normal function: 25

print("Square of", num, "using lambda function:", square_lambda(num))
# Output: Square of 5 using lambda function: 25

# Explanation:
# - The code showcases the concept of anonymous functions or lambda functions.
# - A normal function 'squareIt' is defined to calculate the square of a number.
# - A lambda function 'square_lambda' is defined using the lambda keyword.
# - The lambda function takes an argument and returns its square, all in a concise form.
# - Example usage demonstrates the use of both the normal function and the lambda function.
