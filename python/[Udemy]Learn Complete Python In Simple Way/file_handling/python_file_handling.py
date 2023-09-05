# File handling in Python

# Types of Files:
# There are two types of files: text and binary.

# Opening a File:
# Before performing any operation (like read or write) on the file, we need to open it using the `open()` function.
# We must specify a mode that represents the purpose of opening the file.

# Allowed modes in Python:
# 1) 'r' -> open an existing file for read operation.
#    - The file pointer is positioned at the beginning of the file.
#    - If the specified file does not exist, we will get a FileNotFoundError. This is the default mode.
# 2) 'w' -> open an existing file for write operation.
#    - If the file already contains some data, it will be overridden.
#    - If the specified file is not already available, this mode will create that file.
# 3) 'a' -> open an existing file for append operation.
#    - It won't override existing data.
#    - If the specified file is not already available, this mode will create a new file.
# 4) 'r+' -> To read and write data into the file.
#    - The previous data in the file will not be deleted.
#    - The file pointer is placed at the beginning of the file.
# 5) 'w+' -> To write and read data.
#    - It will override existing data.
# 6) 'a+' -> To append and read data from the file.
#    - It won't override existing data.
# 7) 'x' -> To open a file in exclusive creation mode for write operation.
#    - If the file already exists, we will get a FileExistsError.
# Note: All the above modes are applicable for text files. If suffixed with 'b', they represent binary files.
# Eg: rb, wb, ab, r+b, w+b, a+b, xb

# Example: Opening a file "abc.txt" for writing data
f = open("abc.txt", "w")

# It's essential to close the file after completing operations to free up system resources.
# We use the `close()` function for this purpose.
f.close()
