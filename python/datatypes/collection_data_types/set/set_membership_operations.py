# Membership Operators (in, not in) in Set:

s = set("durga")
print(s)         # {'u', 'g', 'r', 'd', 'a'}
print('d' in s)  # True
print('z' in s)  # False

# Explanation:
# We created a set 's' from the string "durga". When we print the set, it displays the unique characters present in the string.
# Using the 'in' operator, we can check if a specific element (character) exists in the set 's'. In this case, 'd' is present in the set, so the result is True.
# On the other hand, 'z' is not present in the set, so the result is False.
# The 'in' operator returns True if the element exists in the set, and False otherwise.
