# for loop
s = "Nakul Timmesh"
for x in s:  # Loop through each character in the string 's'
    print(x, end=' ')  # Print each character
print()
s = input("Enter some String: ")
i = 0
for x in s:  # Loop through each character in the string 's'
    print("The character present at ", i, "index is:", x, end=' ')  # Print character at the current index 'i'
    i = i + 1  # Increment the index 'i' for the next iteration
print()
for x in range(10):  # Loop through the range from 0 to 9
    print("Hello", end=' ')  # Print "Hello" 10 times

for x in range(11):  # Loop through the range from 0 to 10
    print(x, end=' ')  # Print the numbers from 0 to 10

for x in range(21):  # Loop through the range from 0 to 20
    if (x % 2 != 0):  # Check if the number is odd
        print(x, end=' ')  # Print odd numbers

for x in range(10, 0, -1):  # Loop through the range from 10 to 1 in descending order
    print(x, end=' ')  # Print the numbers from 10 to 1 in descending order

lst = eval(input("Enter List:"))  # Enter a list, e.g., [10, 20, 30, 40]
sum = 0
for x in lst:  # Loop through each element in the list 'lst'
    sum = sum + x  # Add each element to the 'sum'
print("The Sum=", sum)  # Print the sum of the numbers in the list

# while loop
x = 1
while x <= 10:  # Execute the loop until 'x' becomes greater than 10
    print(x)  # Print the value of 'x'
    x = x + 1  # Increment 'x' by 1 in each iteration

n = int(input("Enter number:"))
sum = 0
i = 1
while i <= n:  # Execute the loop until 'i' becomes greater than 'n'
    sum = sum + i  # Add the value of 'i' to 'sum'
    i = i + 1  # Increment 'i' by 1 in each iteration
print("The sum of first", n, "numbers is:", sum)  # Print the sum of first 'n' numbers

name = ""
while name != "Nakul":  # Execute the loop until 'name' is not equal to "Nakul"
    name = input("Enter Name:")  # Prompt the user to enter a name
print("Thanks for confirmation")  # Print the message after the loop

# Infinite loop
# i = 0
# while True:  # This loop will run indefinitely as the condition is always True
#     i = i + 1
#     print("Hello", i)

# Nested loops
for i in range(4):  # Outer loop runs from 0 to 3
    for j in range(4):  # Inner loop also runs from 0 to 3 for each iteration of the outer loop
        print("i=", i, " j=", j)  # Print the values of 'i' and 'j' for each iteration of the nested loops


# Using for loop by length to iterate through characters in a string

s = "Hello!"

# Get the length of the string using len() function
length_of_string = len(s)

for i in range(length_of_string):
    print("Character at index", i, "is:", s[i], end=' ')

