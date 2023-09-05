input_str = input('Enter the string: ')
count_map = {}

# Count the occurrences of each character
for ch in input_str:
    count_map[ch] = count_map.get(ch, 0) + 1

# Create a list to store the key-value pairs
key_value_pairs = []

# Populate the list with formatted strings
for k, v in count_map.items():
    key_value_pairs.append(f'{k}:{v}')

# Join the key-value pairs with a comma and space
result = ', '.join(key_value_pairs)

# Print the result
print(result)
