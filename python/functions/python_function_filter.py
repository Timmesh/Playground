## filter() Function
# - The filter() function is used to filter values from a given sequence based on a certain condition.

# Syntax of filter() function
# filter(function, sequence)

# Where:
# - 'function' is responsible for performing the conditional check.
# - 'sequence' is the list, tuple, or string from which values will be filtered.

# Program to filter even numbers from a list using filter() function

# Approach 1: Without Lambda Function
def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

numbers = [0, 5, 10, 15, 20, 25, 30]
even_numbers = list(filter(isEven, numbers))
print("Even numbers:", even_numbers)
# Output: Even numbers: [0, 10, 20, 30]

# Approach 2: With Lambda Function
numbers = [0, 5, 10, 15, 20, 25, 30]
even_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers (using lambda):", even_numbers_lambda)
# Output: Even numbers (using lambda): [0, 10, 20, 30]

# Filtering odd numbers using lambda function
odd_numbers_lambda = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers (using lambda):", odd_numbers_lambda)
# Output: Odd numbers (using lambda): [5, 15, 25]

# Explanation:
# - The code demonstrates the use of the filter() function to filter values from a sequence.
