def custom_sort(input_str):
    # Separate alphabet symbols and digits
    alpha_chars = []
    digit_chars = []
    for c in input_str:
        if c.isalpha():
            alpha_chars.append(c)
        elif c.isdigit():
            digit_chars.append(c)

        # Sort both sets of characters
    sorted_alpha = ''.join(sorted(alpha_chars))
    sorted_digits = ''.join(sorted(digit_chars))

    # Concatenate alphabet symbols and digits
    sorted_str = ''.join(sorted(alpha_chars) + sorted(digit_chars))

    return sorted_str


# Input string
input_string = input("Enter a string containing alphabet symbols and digits: ")

# Call the custom_sort function and print the sorted string
sorted_string = custom_sort(input_string)
print("Sorted String:", sorted_string)
