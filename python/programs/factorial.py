# Recursive Function to Calculate Factorial

def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Args:
        n (int): The input number

    Returns:
        int: The factorial of the input number
    """
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result

# Example Usage:
print("Factorial of 4 is:", factorial(4))
# Output: Factorial of 4 is: 24

print("Factorial of 5 is:", factorial(5))
# Output: Factorial of 5 is: 120

# Explanation:
# - The function 'factorial' calculates the factorial of a given number 'n'.
# - It uses a recursive approach where it reduces the problem into smaller subproblems.
# - If the input 'n' is 0, the base case returns 1, as 0! = 1.
# - Otherwise, it calculates 'n * factorial(n-1)' to solve the problem recursively.
# - The result is returned to the caller.
# - Example usage demonstrates the calculation of factorial for different numbers.
