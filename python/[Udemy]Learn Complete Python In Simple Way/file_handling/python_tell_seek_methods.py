# The seek() and tell() methods are used to manage the cursor (file pointer) position within a file.

# tell():
# We use the tell() method to return the current position of the cursor (file pointer) from the beginning of the file.
# The position (index) of the first character in files is zero, similar to string indexing.

# Example:
f = open("abc.txt", "r")
print(f.tell())  # Initially, the cursor is at position 0
print(f.read(2))  # Read the first 2 characters
print(f.tell())  # After reading 2 characters, the cursor is at position 2
print(f.read(3))  # Read the next 3 characters
print(f.tell())  # After reading 3 characters, the cursor is at position 5

# seek():
# We use the seek() method to move the cursor (file pointer) to a specified location within the file.
# The seek method takes two arguments: offset and fromwhere.
# - offset represents the number of positions to move.
# - fromwhere specifies the reference point (0 for the beginning of the file, 1 for the current position, 2 for the end of the file).

# Example:
data = "All Students are STUPIDS"
with open("abc.txt", "w") as f:
    f.write(data)

with open("abc.txt", "r+") as f:
    text = f.read()
    print(text)  # Output: "All Students are STUPIDS"
    print("The Current Cursor Position: ", f.tell())  # Output: The cursor is at position 24
    f.seek(17)  # Move the cursor to position 17
    print("The Current Cursor Position: ", f.tell())  # Output: The cursor is at position 17
    f.write("GEMS!!!")  # Overwrite part of the text
    f.seek(0)  # Move the cursor back to the beginning of the file
    text = f.read()
    print("Data After Modification:")
    print(text)  # Output: "All Students are GEMS!!!"
