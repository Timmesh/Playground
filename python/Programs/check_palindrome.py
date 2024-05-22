# Function to check if a string is a palindrome
def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    input_string = input_string.replace(" ", "").lower()

    # Compare the original string with its reverse
    return input_string == input_string[::-1]

# Input a string
str_to_check = input("Enter a string: ")

# Check if it's a palindrome
if is_palindrome(str_to_check):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")