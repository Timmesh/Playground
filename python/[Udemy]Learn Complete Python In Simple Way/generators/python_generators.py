# Create a generator expression that yields the square of each number in the range from 0 to 10
g = (x * x for x in range(11))

# Printing the generator object itself will not display its values
print(g)  # Output: <generator object <genexpr> at 0xXXXXXXXX>

# Use a for loop to iterate through the generator and print each squared value
for x in g:
    print(x)
