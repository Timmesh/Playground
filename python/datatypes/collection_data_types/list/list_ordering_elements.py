# Ordering Elements of List:

# reverse(): We can use reverse() to reverse the order of elements of the list.
n = [10, 20, 30, 40]
n.reverse()
print(n)  # Output: [40, 30, 20, 10]

# sort(): By default, the insertion order is preserved in the list.
# If we want to sort the elements of the list according to the default natural sorting order,
# then we should use the sort() method.
n = [20, 5, 15, 10, 0]
n.sort()
print(n)  # Output: [0, 5, 10, 15, 20]

s = ["Dog", "Banana", "Cat", "Apple"]
s.sort()
print(s)  # Output: ['Apple', 'Banana', 'Cat', 'Dog']

# To Sort in Reverse of Default Natural Sorting Order:
# We can sort according to the reverse of the default natural sorting order by using reverse=True argument.
n = [40, 10, 30, 20]
n.sort()
print(n)  # Output: [10, 20, 30, 40]
n.sort(reverse=True)
print(n)  # Output: [40, 30, 20, 10]
n.sort(reverse=False)
print(n)  # Output: [10, 20, 30, 40]
