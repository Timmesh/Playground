def remove_duplicates(input_string):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through the input string
    for char in input_string:
        # If the character is not already in the result string, add it
        if char not in result:
            result += char

    return result


# Input string
input_string = input("Enter the input string: ")

# Call the remove_duplicates function and print the result
result_string = remove_duplicates(input_string)
print("String after removing duplicates:", result_string)
