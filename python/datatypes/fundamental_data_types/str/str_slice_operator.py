# Slice operation on string 's'
s = 'NAKUL'

# Slicing from index 0 to 4 (end index exclusive)
print(s[0:4])  # Output: 'NAKU'

# Slicing from index 1 to the end of the string
print(s[1:])  # Output: 'AKUL'

# Slicing from the beginning to index 3 (end index exclusive)
print(s[:3])  # Output: 'NAK'

# Slicing the entire string (start to end)
print(s[:])  # Output: 'NAKUL'

# Combining sliced parts to form a new string (convert first letter to lowercase)
print(s[0] + s[1:].lower())  # Output: 'Nakul'

# Slicing the string 's' with various combinations of begin, end, and step values
s = "Learning Python is very very easy!!!"
print(s[1:7:1])  # Output: 'earning'
print(s[1:7])  # Output: 'earning'
print(s[1:7:2])  # Output: 'ern'
print(s[:7])  # Output: 'Learning'
print(s[7:])  # Output: ' Python is very very easy!!!'
print(s[::])  # Output: 'Learning Python is very very easy!!!'
print(s[:])  # Output: 'Learning Python is very very easy!!!'
print(s[::-1])  # Output: '!!!ysae yrev yrev si nohtyP gninraeL'

# Behavior of the slice operator
S = 'abcdefghij'
print(S[1:6:2])  # Output: 'bdf'
print(S[::1])  # Output: 'abcdefghij'
print(S[::-1])  # Output: 'jihgfedcba'
print(S[3:7:-1])  # Output: ''
print(S[7:4:-1])  # Output: 'hgf'
print(S[0:10000:1])  # Output: 'abcdefghij'
print(S[-4:1:-1])  # Output: 'gfedc'
print(S[-4:1:-2])  # Output: 'gec'
print(S[5:0:1])  # Output: ''
# ValueError: slice step cannot be zero (step should not be zero)
# print(S[9:0:0])
print(S[0:-10:-1])  # Output: ''
print(S[0:-11:-1])  # Output: 'a'
print(S[0:0:1])  # Output: ''
print(S[0:-9:-2])  # Output: ''
print(S[-5:-9:-2])  # Output: 'fd'
print(S[10:-1:-1])  # Output: ''
print(S[10000:2:-1])  # Output: 'jihgfed'
