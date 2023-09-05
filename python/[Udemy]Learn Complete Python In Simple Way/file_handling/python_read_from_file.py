# Reading Character Data from Text Files:

# We can read character data from a text file using various read methods:
# 1) read(): Reads the entire content of the file.
# 2) read(n): Reads 'n' characters from the file.
# 3) readline(): Reads one line from the file.
# 4) readlines(): Reads all lines from the file into a list.
# Example 1: Reading the entire content of the file using read()

f = open("abc.txt", 'r')  # Open the file in read ('r') mode
data = f.read()          # Read the entire content of the file
print("Example 1 - Reading the entire content:")
print(data)
f.close()                # Close the file

# Output:
# sunny
# bunny
# chinny
# vinny

# Example 2: Reading 'n' characters from the file using read(n)
f = open("abc.txt", 'r')  # Open the file in read ('r') mode
n = 10                    # Specify the number of characters to read
data = f.read(n)          # Read 'n' characters from the file
print("\nExample 2 - Reading", n, "characters:")
print(data)
f.close()

# Output:
# sunny
# bunn

# Example 3: Reading one line from the file using readline()
f = open("abc.txt", 'r')     # Open the file in read ('r') mode
line1 = f.readline()         # Read the first line from the file
print("\nExample 3 - Reading one line:")
print(line1, end='')         # Print the first line
f.close()

# Output:
# sunny

# Example 4: Reading all lines from the file into a list using readlines()
f = open("abc.txt", 'r')     # Open the file in read ('r') mode
lines = f.readlines()        # Read all lines from the file into a list
print("\nExample 4 - Reading all lines into a list:")
for line in lines:
    print(line, end='')      # Print each line from the list
f.close()

# Output:
# sunny
# bunny
# chinny
# vinny
