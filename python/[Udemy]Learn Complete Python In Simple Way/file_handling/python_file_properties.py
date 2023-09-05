# Various Properties of File Object:

# Once we open a file and obtain a file object, we can access various details related to that file
# by using its properties.

# Properties of a File Object:
# - name: Name of the opened file.
# - mode: Mode in which the file is opened.
# - closed: Returns a boolean value indicating whether the file is closed or not.
# - readable(): Returns a boolean value indicating whether the file is readable or not.
# - writable(): Returns a boolean value indicating whether the file is writable or not.

# Example:
# Opening a file "abc.txt" in write mode ('w')
f = open("abc.txt", 'w')

# Accessing file properties
print("File Name: ", f.name)              # Print the name of the file
print("File Mode: ", f.mode)              # Print the mode in which the file is opened
print("Is File Readable: ", f.readable())  # Check if the file is readable and print the result
print("Is File Writable: ", f.writable())  # Check if the file is writable and print the result

# At this point, the file is open, so it is not closed
print("Is File Closed : ", f.closed)       # Check if the file is closed and print the result

# Close the file to free up system resources
f.close()

# After closing the file, it is considered closed
print("Is File Closed : ", f.closed)       # Check if the file is closed and print the result
