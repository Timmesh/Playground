# ## map() Function
#
# # Introduction to the map() function
# # - The map() function is used to apply a given functionality to each element in a sequence and generate a new sequence with the required modifications.
#
# # Syntax of map() function
# # map(function, sequence)
#
# # Where:
# # - 'function' is applied to each element of the sequence.
# # - 'sequence' is the list, tuple, or other iterable.
#
# # Example 1: Doubling each element in a list
#
# # Approach 1: Without Lambda
# def doubleIt(x):
#     """
#     Double the input number.
#
#     Args:
#         x (int): The input number
#
#     Returns:
#         int: The doubled value of the input number
#     """
#     return 2 * x
#
# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = list(map(doubleIt, numbers))
# print("Doubled numbers:", doubled_numbers)
# # Output: Doubled numbers: [2, 4, 6, 8, 10]
#
# # Approach 2: With Lambda
# numbers = [1, 2, 3, 4, 5]
# doubled_numbers_lambda = list(map(lambda x: 2 * x, numbers))
# print("Doubled numbers (using lambda):", doubled_numbers_lambda)
# # Output: Doubled numbers (using lambda): [2, 4, 6, 8, 10]
#
# # Example 2: Finding the square of each element
#
# numbers = [1, 2, 3, 4, 5]
# squared_numbers_lambda = list(map(lambda x: x * x, numbers))
# print("Squared numbers (using lambda):", squared_numbers_lambda)
# # Output: Squared numbers (using lambda): [1, 4, 9, 16, 25]
#
# # Applying map() function on multiple lists
# # Here, the elements from l1 and l2 are multiplied element-wise
#
# l1 = [1, 2, 3, 4]
# l2 = [2, 3, 4, 5]
# result_list = list(map(lambda x, y: x * y, l1, l2))
# print("Resultant list (using map):", result_list)
# # Output: Resultant list (using map): [2, 6, 12, 20]
#
# # Explanation:
# # - The code illustrates the use of the map() function to apply a given functionality to each element of a sequence.
# # - Two examples are provided: doubling numbers and finding the square of numbers.
# # - Both approaches, with and without a lambda function, are demonstrated for each example.
# # - The concept of applying map() to multiple lists (element-wise) is also explained.

