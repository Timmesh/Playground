# Garbage Collection

# Explanation of Garbage Collection in Python
# Garbage collection in Python refers to the process of automatically identifying and
# reclaiming memory that is no longer needed by the program. This helps in freeing up memory
# resources and preventing memory leaks.
# Python uses a built-in garbage collector to manage memory and automatically clean up objects
# that are no longer in use. The garbage collector keeps track of the reference count of objects
# and uses reference cycles to determine which objects are still reachable (i.e., in use) and
# which are not. Objects that are no longer reachable are considered garbage and are collected.

# If an object does not have any reference variable then that object is eligible for Garbage Collection.

# How to enable and disable Garbage Collector in our Program:

# By default, the Garbage collector is enabled, but we can disable it based on our requirement.
# In this context, we can use the following functions of the gc module.
# 1. gc.isenabled() # Returns True if GC enabled
# 2. gc.disable()   # To disable GC explicitly
# 3. gc.enable()    # To enable GC explicitly

import gc

# Check if the Garbage Collector is enabled
print(gc.isenabled())  # True

# Disable the Garbage Collector
gc.disable()
print(gc.isenabled())  # False

# Enable the Garbage Collector
gc.enable()
print(gc.isenabled())  # True
