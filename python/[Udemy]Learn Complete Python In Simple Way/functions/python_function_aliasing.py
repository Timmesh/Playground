## Function Aliasing

# - Function aliasing involves giving an existing function another name.

# Example: Function Aliasing

# Defining the function 'wish'
def wish(name):
    print("Good Morning:", name)

# Creating an alias 'greeting' for the function 'wish'
greeting = wish

# Displaying the memory address of the original function 'wish'
print(id(wish))  # 4429336

# Displaying the memory address of the alias function 'greeting'
print(id(greeting))  # 4429336

# Calling the function using the alias 'greeting'
greeting('Durga')  # Good Morning: Durga

# Calling the function using the original name 'wish'
wish('Durga')  # Good Morning: Durga

# Explanation:
# - The function 'wish' is defined to print a greeting message.
# - An alias 'greeting' is created for the 'wish' function.
# - The memory addresses of the original function and the alias function are the same, as indicated by 'id(wish)' and 'id(greeting)'.
# - Both 'wish' and 'greeting' can be used interchangeably to call the same function.
# - Even if the original function name 'wish' is deleted using 'del', the alias 'greeting' can still be used to call the function.
# - This demonstrates how function aliasing allows multiple names to refer to the same function.

# Additional Example: Accessing Alias Even After Deleting Original Function

# Defining the function 'wish' again
def wish(name):
    print("Good Morning:", name)

# Creating an alias 'greeting' for the function 'wish'
greeting = wish

# Calling the function using the alias 'greeting'
greeting('Durga')  # Good Morning: Durga

# Calling the function using the original name 'wish'
wish('Durga')  # Good Morning: Durga

# Deleting the original function 'wish'
del wish

# Calling the function using the alias 'greeting' after deleting the original function
greeting('Pavan')  # Good Morning: Pavan

# Note:
# - The alias 'greeting' still works even after the original function 'wish' is deleted.
# - This demonstrates that the alias maintains a reference to the function independently of the original name.
