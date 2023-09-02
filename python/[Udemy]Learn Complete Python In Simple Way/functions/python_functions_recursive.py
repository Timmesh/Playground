# Recursive Functions in Python

# Recursive Function:
# A function that calls itself is known as a recursive function.

# Example: Factorial Calculation
# The factorial of a number is the product of all positive integers less than or equal to that number.

def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Args:
        n (int): The input number

    Returns:
        int: The factorial of the input number
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example Usage:
result = factorial(3)
print("Factorial of 3 =", result)
# Output: Factorial of 3 = 6

result = factorial(5)
print("Factorial of 5 =", result)
# Output: Factorial of 5 = 120

# Recursive Functions Advantages:
# 1. Reduces code length and improves readability.
# 2. Solves complex problems more easily.

# Summary:
# - A recursive function is a function that calls itself.
# - It's useful for solving problems with repetitive or self-similar structures.
# - The base case is essential in recursive functions to prevent infinite recursion.
# - Recursive functions can simplify code and make complex problems more manageable.
