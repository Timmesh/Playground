# Reading Data from a CSV File

# Import the csv module to work with CSV files
import csv

# Open the CSV file 'emp.csv' in read mode ('r')
f = open("emp.csv", 'r')

# Create a CSV reader object using the file handle 'f'
r = csv.reader(f)

# Read all the data from the CSV file into a list 'data'
data = list(r)

# Loop through each row in the 'data' list
for line in data:
    # Loop through each word (cell) in the row
    for word in line:
        # Print each word followed by a tab character ('\t') and no newline character
        print(word, "\t", end='')

    # Print a newline character to move to the next line after processing each row
    print()

# Close the CSV file
f.close()
