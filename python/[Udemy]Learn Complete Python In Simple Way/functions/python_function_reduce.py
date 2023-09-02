## reduce() Function
# - The reduce() function is used to reduce a sequence of elements into a single element by applying the specified function.

# Syntax of reduce() function
# reduce(function, sequence)

# Where:
# - 'function' is applied cumulatively to the items of the sequence, from left to right.
# - 'sequence' is the list, tuple, or other iterable.

# Importing the reduce() function from the functools module
from functools import reduce

# Example 1: Summing up elements in a list

numbers = [10, 20, 30, 40, 50]
sum_result = reduce(lambda x, y: x + y, numbers)
print("Sum of elements:", sum_result)
# Output: Sum of elements: 150

# Example 2: Multiplying elements in a list

product_result = reduce(lambda x, y: x * y, numbers)
print("Product of elements:", product_result)
# Output: Product of elements: 12000000

# Example 3: Sum of numbers from 1 to 100

sum_1_to_100 = reduce(lambda x, y: x + y, range(1, 101))
print("Sum of numbers from 1 to 100:", sum_1_to_100)
# Output: Sum of numbers from 1 to 100: 5050

# Explanation:
# - The code demonstrates the use of the reduce() function to cumulatively apply a given functionality to a sequence of elements.
# - The examples include summing up elements in a list, multiplying elements in a list, and finding the sum of numbers from 1 to 100.
# - The reduce() function is imported from the functools module using the import statement.
# - The lambda function is used to specify the cumulative operation to be applied.

