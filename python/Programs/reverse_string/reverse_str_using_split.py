str = 'reverse string'
strlist = str.split();
reversed_str_list = strlist[::-1]
print(''.join(reversed_str_list))

l=str.split()
l1=[]
for word in l:
    l1.append(word[::-1])
output=' '.join(l1)
print(output)