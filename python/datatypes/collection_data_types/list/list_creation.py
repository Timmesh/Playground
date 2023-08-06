# Python List Creation Examples

# Creation of List Objects
# Example 1: Empty List
empty_list = []
print(empty_list)  # Output: []
print(type(empty_list))  # Output: <class 'list'>

# Example 2: List with Known Elements
known_list = [10, 20, 30, 40]
print(known_list)  # Output: [10, 20, 30, 40]

# Example 3: Dynamic Input for List
input_list = eval(input("Enter List:"))  # Enter List:[10,20,30,40]
print(input_list)  # Output: [10, 20, 30, 40]
print(type(input_list))  # Output: <class 'list'>

# Example 4: Using list() Function with range
l = list(range(0, 10, 2))
print(l)  # Output: [0, 2, 4, 6, 8]
print(type(l))  # Output: <class 'list'>

# Example 5: Using list() Function with string
s = "Nakul"
l = list(s)
print(l)  # Output: ['N', 'a', 'k', 'u', 'l']

# Example 6: Using split() Function with string
s = "Learning Python is very very easy !!!"
l = s.split()
print(l)  # Output: ['Learning', 'Python', 'is', 'very', 'very', 'easy', '!!!']
print(type(l))  # Output: <class 'list'>
