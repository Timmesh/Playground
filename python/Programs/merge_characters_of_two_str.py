def merge_alternatively(str1, str2):
    # Initialize an empty string to store the merged result
    merged_str = ""

    # Get the lengths of both strings
    len1 = len(str1)
    len2 = len(str2)

    # Determine the maximum length between the two strings
    max_len = max(len1, len2)

    # Iterate through both strings up to the maximum length
    for i in range(max_len):
        # Append a character from the first string if it exists
        if i < len1:
            merged_str += str1[i]

        # Append a character from the second string if it exists
        if i < len2:
            merged_str += str2[i]

    return merged_str

# Input strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Call the merge_alternatively function and print the result
result = merge_alternatively(string1, string2)
print("Merged String:", result)
