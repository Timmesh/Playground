# Handling CSV Files: Writing Data to a CSV File

# Import the csv module to work with CSV files
import csv

# Open the CSV file 'emp.csv' in write mode ('w') with newline='' to handle line endings
with open("emp.csv", "w", newline='') as f:

    # Create a CSV writer object using the file handle 'f'
    w = csv.writer(f)

    # Write the header row to the CSV file
    w.writerow(["ENO", "ENAME", "ESAL", "EADDR"])

    # Prompt the user to enter the number of employees
    n = int(input("Enter Number of Employees:"))

    # Loop through each employee to collect data
    for i in range(n):
        eno = input("Enter Employee No:")
        ename = input("Enter Employee Name:")
        esal = input("Enter Employee Salary:")
        eaddr = input("Enter Employee Address:")

        # Write the employee data as a list to the CSV file
        w.writerow([eno, ename, esal, eaddr])

    # Print a message to indicate that all employees' data has been written to the CSV file successfully
    print("Total Employees data written to csv file successfully")
