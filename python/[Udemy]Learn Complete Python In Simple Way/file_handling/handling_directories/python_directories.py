# Working with Directories:

# It is a common requirement to perform operations on directories like:
# 1) To know the current working directory.
# 2) To create a new directory.
# 3) To remove an existing directory.
# 4) To rename a directory.
# 5) To list the contents of a directory, etc.

# To perform these operations, Python provides the built-in 'os' module, which contains several
# functions to handle directory-related operations.

# Q1) To Know the Current Working Directory
import os
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# Q2) To Create a Subdirectory in the Current Working Directory
import os
os.mkdir("mysub")
print("mysub directory created in the current working directory")

# Q3) To Create a Subdirectory in the 'mysub' Directory
# Assuming 'mysub' already exists in the current working directory.
# Directory structure:
# cwd
# |-mysub
# |-mysub2
import os
os.mkdir("mysub/mysub2")
print("mysub2 created inside mysub")

# Q4) To Create Multiple Directories like 'sub1' in 'sub2' in 'sub3'
import os
os.makedirs("sub1/sub2/sub3")
print("sub1, sub2, and sub3 directories created")

# Q5) To Remove a Directory
import os
os.rmdir("mysub/mysub2")
print("mysub2 directory deleted")

# Q6) To Remove Multiple Directories in the Path
import os
os.removedirs("sub1/sub2/sub3")
print("All three directories sub1, sub2, and sub3 removed")

# Q7) To Rename a Directory
import os
os.rename("mysub", "newdir")
print("mysub directory renamed to newdir")

# Q8) To Know Contents of a Directory
# The 'os' module provides the 'listdir()' function to list the contents of the specified directory.
# It won't display the contents of subdirectories.
import os
print("List of Contents in the Current Directory:")
print(os.listdir("."))

# Q9) To Know Contents of Directory including Subdirectories
# We use the 'walk()' function, which returns an Iterator object whose contents can be displayed using a for loop.
# path → Directory Path. 'cwd' means current directory.
# topdown = True → Travel from top to bottom.
# onerror = None → On error detected, which function to execute.
# followlinks = True → To visit directories pointed to by symbolic links.
# Example: To display all contents of the current working directory including subdirectories:
for dirpath, dirnames, filenames in os.walk('.'):
    print("Current Directory Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)
    print()

# Note: To display contents of a particular directory, provide that directory name as an argument to the 'walk()' function.
# os.walk("directoryname")

# Difference between listdir() and walk() Functions:
# In the case of 'listdir()', we get the contents of the specified directory but not subdirectory contents.
# In the case of the 'walk()' function, we get the contents of the specified directory and its subdirectories as well.
