# Handling Binary Data: Reading an Image File and Writing to a New Image File

# Open the source image file 'rossum.jpg' in binary read mode ('rb')
f1 = open("OOPB0700.jpg", "rb")

# Open a new image file 'newpic.jpg' in binary write mode ('wb')
f2 = open("newpic.jpg", "wb")

# Read the binary data from the source image file and store it in the 'bytes' variable
bytes = f1.read()

# Write the binary data from the 'bytes' variable to the new image file 'newpic.jpg'
f2.write(bytes)

# Close both files
f1.close()
f2.close()

# Print a message to indicate that the new image is available with the specified name
print("New Image is available with the name: newpic.jpg")
