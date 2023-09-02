# break statement example
for i in range(10):
    if i == 7:
        print("Processing is enough..please break")
        break
    print(i)

# break statement example with a list
cart = [10, 20, 600, 60, 70]
for item in cart:
    if item > 500:
        print("To place this order insurance must be required")
        break
    print(item)

# continue statement example
# To print odd numbers in the range 0 to 9
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# continue statement example with a list
cart = [10, 20, 500, 700, 50, 60]
for item in cart:
    if item >= 500:
        print("We cannot process this item:", item)
        continue
    print(item)

# continue statement example with division
numbers = [10, 20, 0, 5, 0, 30]
for n in numbers:
    if n == 0:
        print("Hey, we can't divide with zero...just skipping")
        continue
    print("100/{} = {}".format(n, 100 / n))

# for loop with else block example
# The for loop completes its execution, the else block is executed if the loop was not terminated by a break statement during its iterations.
# In other words, if all items in the cart have values less than 500, the else block will be executed.
cart = [10, 20, 30, 40, 50]
for item in cart:
    if item >= 500:
        print("We cannot process this order")
        break
    print(item, end=" ")
else:
    print("Congrats...all items processed successfully")

# nested loops example
for i in range(4):
    for j in range(4):
        print("i=", i, " j=", j)

# pass statement example
for i in range(100):
    if i % 9 == 0:
        print(i, end=" ")
else:
    pass

# del statement example
x = 10
print(x)
del x

# After deleting a variable, we cannot access it
# print(x) # NameError: name 'x' is not defined.

# None assignment example
s = "Nakul"
print(s)
s = None
print(s)  # None
