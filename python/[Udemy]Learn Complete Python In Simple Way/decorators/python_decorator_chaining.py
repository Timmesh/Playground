# Define the first decorator decor1
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

# Define the second decorator decor
def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner

# Apply decor1 and decor decorators to the num function using decorator chaining
@decor1
@decor
def num():
    return 10

# When num() is called, it will go through the decorator chain: decor1 -> decor
result = num()

# Print the result
print(result)  # Output: 400 (10 * 10 * 2)
