# Define a generator function called countdown
def countdown(num):
    print("Start Countdown")
    while num > 0:
        yield num  # Yield the current value of 'num'
        num -= 1  # Decrement 'num' for the next iteration

# Create a generator object by calling the 'countdown' function with an initial value of 5
values = countdown(5)

# Iterate through the generator and print each yielded value
for x in values:
    print(x)
