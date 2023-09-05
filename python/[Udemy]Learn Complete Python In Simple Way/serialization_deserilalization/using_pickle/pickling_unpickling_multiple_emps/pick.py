# Import the Employee class and pickle module
import emp
import pickle

# Open a binary file for writing employee objects
f = open("emp.dat", "wb")

# Get the number of employees from the user
n = int(input("Enter the number of Employees:"))

# Loop to input and pickle multiple employee objects
for i in range(n):
    eno = int(input("Enter Employee Number:"))
    ename = input("Enter Employee Name:")
    esal = float(input("Enter Employee Salary:"))
    eaddr = input("Enter Employee Address:")

    # Create an Employee object
    e = emp.Employee(eno, ename, esal, eaddr)

    # Pickle and write the Employee object to the file
    pickle.dump(e, f)

# Close the file
f.close()
print("Employee Objects pickled successfully")
