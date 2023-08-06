# frozenset Data Type:

# A frozenset is similar to a set, but it is immutable, meaning its elements cannot be modified after creation.
# We can use frozenset() function to create a frozenset from an existing set or any other iterable object.

s = {10, 20, 30, 40}
fs = frozenset(s)

# The variable 'fs' now holds a frozenset object containing the elements from the set 's'.

type(fs)  # <class 'frozenset'>
fs       # frozenset({40, 10, 20, 30})

# Looping through a frozenset is the same as looping through a regular set or any iterable object.
# We can access the elements of the frozenset using a for loop.

for i in fs:
    print(i)  # 40 10 20 30

# Since frozensets are immutable, we cannot use functions like add() or remove() that modify the set.

fs.add(70)     # AttributeError: 'frozenset' object has no attribute 'add'
fs.remove(10)  # AttributeError: 'frozenset' object has no attribute 'remove'

# Attempting to use add() or remove() on a frozenset will raise an AttributeError, as these methods are not available for frozensets.
# This is because frozensets are intended to be used when you need an immutable set.
