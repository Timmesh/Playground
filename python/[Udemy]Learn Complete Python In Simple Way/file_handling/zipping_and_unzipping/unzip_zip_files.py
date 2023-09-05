# To perform an unzip operation, we need to create a ZipFile object as follows:
# Create a ZipFile object 'f' with the name of the zip file, mode 'r' for read, and ZIP_STORED constant.
# ZIP_STORED represents unzip operation, and it is the default value, so specifying it is optional.
from zipfile import ZipFile, ZIP_STORED

# Create a ZipFile object 'f' to open the existing zip file "files.zip" for reading.
f = ZipFile("files.zip", 'r', ZIP_STORED)

# We can obtain a list of all file names present in the zip file using the namelist() method.
names = f.namelist()

# Iterate through the list of file names.
for name in names:
    print("File Name:", name)

    # Print a message indicating the content of the current file.
    print("The Content of this file is:")

    # Open the current file from the zip archive for reading.
    f1 = f.open(name, 'r')

    # Read and print the content of the file.
    print(f1.read())

    # Print an empty line for separation.
    print()
