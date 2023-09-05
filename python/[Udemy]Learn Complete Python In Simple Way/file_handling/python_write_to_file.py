# Writing Data to Text Files:

# We can write character data to text files using the following methods:
# 1) write(str): Writes a single string to the file.
# 2) writelines(list of lines): Writes a list of strings (lines) to the file.

# Example 1: Using the write() method to write individual lines to the file
f = open("abcd.txt", 'w')  # Open the file in write ('w') mode
f.write("Durga\n")         # Write "Durga" followed by a newline character to the file
f.write("Software\n")      # Write "Software" followed by a newline character to the file
f.write("Solutions\n")     # Write "Solutions" followed by a newline character to the file
print("Data written to the file successfully")
f.close()                  # Close the file

# abcd.txt contents after running this code:
# Durga
# Software
# Solutions

# Note: In the above program, data present in the file will be overridden every time
# if we run the program. To perform an append operation instead of overriding, open
# the file as follows:
# f = open("abcd.txt", "a")

# Example 2: Using the writelines() method to write a list of lines to the file
f = open("abcd.txt", 'w')            # Open the file in write ('w') mode
lines = ["sunny\n", "bunny\n", "vinny\n", "chinny"]  # Create a list of lines
f.writelines(lines)                 # Write the list of lines to the file
print("List of lines written to the file successfully")
f.close()                            # Close the file

# abcd.txt contents after running this code:
# sunny
# bunny
# vinny
# chinny

# Note: While using the write() method, you must provide a line separator (\n) to
# ensure each string is written on a new line. Otherwise, all data will be written
# to a single line.
