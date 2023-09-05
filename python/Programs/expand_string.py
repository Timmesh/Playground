# Write a program for the following requirement?
# 1) input: ac3b4
# 2) output: acacacbbb

def expand_string(input_str):
    expanded_str = ""
    i = 0
    char = ''
    while i < len(input_str):
        char = char + input_str[i]
        i += 1
        if (input_str[i].isalpha()): continue

        count = 0
        while i < len(input_str) and input_str[i].isdigit():
            count = count * 10 + int(input_str[i])
            i += 1

        expanded_str += char * count
        char = ''

    return expanded_str


# Input string
input_string = input("Enter the input string: ")

# Call the expand_string function and print the expanded string
expanded_string = expand_string(input_string)
print("Expanded String:", expanded_string)
