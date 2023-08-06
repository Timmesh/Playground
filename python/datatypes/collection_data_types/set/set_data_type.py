# Set Data Type:

# If we want to represent a group of values without duplicates where order is not important,
# then we should use the set Data Type.

# Characteristics of set Data Type:
# 1. Insertion order is not preserved.
# 2. Duplicates are not allowed.
# 3. Heterogeneous objects are allowed.
# 4. Index concept is not applicable.
# 5. It is a mutable collection.
# 6. Growable in nature.

# We can represent set elements within curly braces {} with comma separation.

s = {100, 0, 10, 200, 10, 'durga'}
print(s)  # {0, 100, 'durga', 200, 10}

# Explanation:
# The set automatically removes duplicates, so even though we have two occurrences of 10,
# only one occurrence is retained in the set.

# Index concept is not applicable for set

# s[0]  # TypeError: 'set' object does not support indexing

# Explanation:
# Since sets do not preserve insertion order and do not support indexing,
# trying to access elements using an index like s[0] will raise a TypeError.

# We can apply mathematical operations like union, intersection, difference, etc., on set objects.

# Example of set operations:

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union_set = set1.union(set2)
print(union_set)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection of sets
intersection_set = set1.intersection(set2)
print(intersection_set)  # {4, 5}

# Difference of sets
difference_set = set1.difference(set2)
print(difference_set)  # {1, 2, 3}

# Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # {1, 2, 3, 6, 7, 8}

# Sets are growable in nature. We can add or remove elements as needed.

s.add(60)
print(s)  # {0, 100, 'durga', 200, 10, 60}

s.remove(100)
print(s)  # {0, 'durga', 200, 10, 60}

# Explanation:
# We can add an element to the set using the add() method and remove an element using the remove() method.
# In this example, we added 60 to the set and then removed 100 from the set.
# The set dynamically adjusts its size based on the elements we add or remove.
