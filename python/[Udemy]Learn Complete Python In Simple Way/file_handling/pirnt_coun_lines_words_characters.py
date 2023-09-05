# Program to print the number of lines, words, and characters present in the given file.

# Import the required modules
import os
import sys

# Get the file name from the user
fname = input("Enter File Name: ")

# Check if the file exists
if os.path.isfile(fname):
    print("File exists:", fname)
    f = open(fname, "r")  # Open the file in read mode
else:
    print("File does not exist:", fname)
    sys.exit(0)  # Exit the program if the file does not exist

# Initialize counters for lines, words, and characters
lcount = wcount = ccount =lencount= 0

# Iterate through each line in the file
for line in f:
    lcount = lcount + 1  # Increment the line count for each line
    lencount = ccount + len(line)  # Add the length of the line to character count
    words = line.split(' ')  # Split the line into words using whitespace as a separator
    wcount = wcount + len(words)  # Increment the word count by the number of words in the line
    for word in words:
        ccount += len(word)

# Print the results
print("The number of Lines:", lcount)
print("The number of Words:", wcount)
print("The number of Characters:", ccount)
print("The number of Characters with space:", lencount)
# Close the file
f.close()
