# Import the Employee class and pickle module
import emp
import pickle

# Open the binary file for reading employee objects
f = open("emp.dat", "rb")

print("Employee Details:")

# Loop to unpickle and display employee objects
while True:
    try:
        # Unpickle an Employee object from the file
        obj = pickle.load(f)
        obj.display()
    except EOFError:
        # EOFError indicates the end of file
        print("All employees completed")
        break

# Close the file
f.close()
