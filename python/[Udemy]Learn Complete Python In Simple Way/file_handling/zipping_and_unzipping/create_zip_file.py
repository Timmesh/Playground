# Zipping and Unzipping Files

# Import the necessary functions and classes from the zipfile module
from zipfile import ZipFile, ZIP_DEFLATED

# It is a common requirement to zip and unzip files for various advantages,
# including improving memory utilization, reducing transport time, and enhancing performance.

# To perform zip operations, Python provides the built-in zip file module, which contains the ZipFile class.

# To create a Zip File:
# Create a ZipFile object with the name of the zip file, mode 'w' for write, and ZIP_DEFLATED constant for zip compression.
f = ZipFile("files.zip", 'w', ZIP_DEFLATED)

# Add files to the zip file using the write() method of the ZipFile object.
f.write("file1.txt")
f.write("file2.txt")
f.write("file3.txt")

# Close the zip file to save the changes.
f.close()

# Print a message indicating that the zip file has been created successfully.
print("files.zip file created successfully")
