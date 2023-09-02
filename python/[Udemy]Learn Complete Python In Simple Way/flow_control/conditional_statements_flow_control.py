# if
name = input("Enter Name:")
if name == "Nakul":  # If condition is true then the following statement will be executed.
    print("Hello Nakul Good Morning")
print("How are you!!!")

# if-else
name = input("Enter Name:")
if name == "Nakul":  # If condition is true then the following statement will be executed.
    print("Hello Nakul Good Morning")
else:  # If condition is false then the following statement will be executed.
    print("Hello Guest Good Morning")
print("How are you!!!")

# if-elif-else
brand = input("Enter Your Favourite Brand:")
if brand == "RC":  # If condition1 is true then Action-1 will be executed.
    print("It is children's brand")
elif brand == "KF":  # If condition1 is false and condition2 is true then Action-2 will be executed.
    print("It is not that much kick")
elif brand == "FO":  # If condition1 and condition2 are false and condition3 is true then Action-3 will be executed.
    print("Buy one get Free One")
else:  # If all conditions are false then Default Action will be executed.
    print("Other Brands are not recommended")
