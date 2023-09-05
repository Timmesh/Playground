def remove_duplicates(input_string):
    # Convert the input string to a set to remove duplicates
    unique_chars = set(input_string)

    # Join the unique characters back into a string
    result_string = ''.join(unique_chars)

    return result_string

# Input string
input_string = input("Enter the input string: ")

# Call the remove_duplicates function and print the result
result_string = remove_duplicates(input_string)
print("String after removing duplicates:", result_string)
