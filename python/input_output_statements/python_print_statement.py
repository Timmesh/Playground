# Form-1: print() without any argument
print()  # Just prints a new line character

# Form-2: print(String)
print("Hello World")
print("Hello \n World")  # Uses escape characters for newline and tab
print(10 * "Hello")  # Repetition operator (*) in the string
print("Hello" + "World")  # Uses + operator to concatenate strings

# Form-3: print() with variable number of arguments and "sep" attribute
a, b, c = 10, 20, 30
print("The Values are:", a, b, c)  # Outputs with default separator (space)
print(a, b, c, sep=',')  # Outputs values with ',' as separator
print(a, b, c, sep=':')  # Outputs values with ':' as separator

# Form-4: print() with "end" attribute
print("Hello")  # Prints "Hello" and a new line
print("Durga")  # Prints "Durga" and a new line
print("Soft")  # Prints "Soft" and a new line

print("Hello", end=' ')  # Outputs "Hello " with a space instead of a new line
print("Durga", end=' ')  # Outputs "Durga " with a space instead of a new line
print("Soft")  # Outputs "Soft" with a new line at the end

# Form-5: print(object) statement
l = [10, 20, 30, 40]
t = (10, 20, 30, 40)
print(l)  # Outputs the list [10, 20, 30, 40]
print(t)  # Outputs the tuple (10, 20, 30, 40)

# Form-6: print(String, variable list)
s = "Nakul"
a = 48
s1 = "Java"
s2 = "Python"
print("Hello", s, "Your Age is", a)  # Outputs a formatted string
print("You are teaching", s1, "and", s2)  # Outputs a formatted string

# Form-7: print (formatted string)
a = 10
b = 20
c = 30
print("a value is %i" % a)  # Outputs a formatted string using %i as int placeholder
print("b value is %d and c value is %d" % (b, c))  # Outputs multiple values in a formatted string

s = "Durga"
list_items = [10, 20, 30, 40]
print("Hello %s ...The List of Items are %s" % (
s, list_items))  # Outputs a formatted string using %s as string placeholder

# Form-8: print() with replacement operator {}
name = "Durga"
salary = 10000
gf = "Sunny"
print("Hello {0} your salary is {1} and Your Friend {2} is waiting".format(name, salary,
                                                                           gf))  # Outputs a formatted string using positional arguments
print("Hello {x} your salary is {y} and Your Friend {z} is waiting".format(x=name, y=salary,
                                                                           z=gf))  # Outputs a formatted string using keyword arguments
