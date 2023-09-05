# How to get Information about a File:

# We can retrieve statistics of a file, such as its size, last accessed time, last modified time, etc.,
# by using the 'stat()' function from the 'os' module.

# To get file statistics, use the following syntax:
# stats = os.stat("abc.txt")

# The statistics of a file include the following parameters:
# 1) st_mode    -> Protection Bits
# 2) st_ino     -> Inode number
# 3) st_dev     -> Device
# 4) st_nlink   -> Number of Hard Links
# 5) st_uid     -> User id of Owner
# 6) st_gid     -> Group id of Owner
# 7) st_size    -> Size of File in Bytes
# 8) st_atime   -> Time of Most Recent Access
# 9) st_mtime   -> Time of Most Recent Modification
# 10) st_ctime  -> Time of Most Recent Meta Data Change

# Note: 'st_atime', 'st_mtime', and 'st_ctime' return the time as the number of milliseconds since
#       Jan 1st, 1970, 12:00 AM. We can use the 'datetime' module to convert these timestamps
#       to human-readable date and time.

# Example: To Print all Statistics of File 'abc.txt'
import os
stats = os.stat("abc.txt")
print(stats)

# Example: To Print specified Properties
from datetime import datetime
stats = os.stat("abc.txt")
print("File Size in Bytes:", stats.st_size)
print("File Last Accessed Time:", datetime.fromtimestamp(stats.st_atime))
print("File Last Modified Time:", datetime.fromtimestamp(stats.st_mtime))
