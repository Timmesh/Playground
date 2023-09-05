# The with statement can be used while opening a file.
# It allows us to group file operation statements within a block.
# The advantage of using with is that it takes care of closing the file automatically,
# even in the case of exceptions, and we are not required to close it explicitly.

# Example:
# Open the file "abc.txt" in write ('w') mode and assign it to the variable 'f'.
# The 'with' statement ensures that the file will be automatically closed when the block is exited.
with open("../abc.txt", "w") as f:
    # Write data to the file
    f.write("Durga\n")
    f.write("Software\n")
    f.write("Solutions\n")

# The file is automatically closed when we exit the 'with' block.
# We can check if the file is closed using the 'closed' property of the file object.
print("Is File Closed: ", f.closed)  # Should print True
# Since the file is already closed outside the 'with' block, it's still closed here.
print("Is File Closed: ", f.closed)  # Should print True
