# Overloading Examples:

# Operator Overloading Example:
# The + operator is overloaded for both arithmetic addition and string concatenation.
print(10 + 20)  # Arithmetic addition: 30
print('durga' + 'soft')  # String concatenation: durgasoft

# The * operator is overloaded for both multiplication and string repetition.
print(10 * 20)  # Multiplication: 200
print('durga' * 3)  # String repetition: durgadurgadurga

# Method Overloading Example:
# We can use the deposit() method to deposit cash, cheque, or dd (demand draft).
def deposit(payment_method):
    if payment_method == 'cash':
        print('Depositing cash...')
    elif payment_method == 'cheque':
        print('Depositing cheque...')
    elif payment_method == 'dd':
        print('Depositing demand draft...')

deposit('cash')  # Depositing cash
deposit('cheque')  # Depositing cheque
deposit('dd')  # Depositing demand draft

# Constructor Overloading Example:
# Constructor overloading is not directly supported in Python.
# However, we can achieve similar behavior using default values and optional parameters.
class Student:
    def __init__(self, name=None, roll=None):
        self.name = name
        self.roll = roll

# Creating instances with different constructor arguments
student1 = Student()  # No arguments provided
student2 = Student('John')  # Only name provided
student3 = Student('Alice', 101)  # Both name and roll provided

print(student1.name, student1.roll)  # None None
print(student2.name, student2.roll)  # John None
print(student3.name, student3.roll)  # Alice 101
