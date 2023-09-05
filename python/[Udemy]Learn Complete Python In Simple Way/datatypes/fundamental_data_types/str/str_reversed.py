str = input("Enter str to be reversed");
revStrObj = reversed(str)
for item in revStrObj:
    print(item,end='')
print()
revStrObj = reversed(str)
print(''.join(revStrObj))