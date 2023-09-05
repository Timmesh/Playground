# Pickling and Unpickling of Objects:

# Sometimes, we need to store the entire state of an object to a file and then retrieve it later.
# The process of writing the state of an object to a file is called pickling, and the process of
# reading the state of an object from a file is called unpickling.

# Python provides the 'pickle' module to implement pickling and unpickling.

# To perform pickling, we use the 'dump()' function from the 'pickle' module, as follows:
# pickle.dump(object, file)

# To perform unpickling, we use the 'load()' function from the 'pickle' module, as follows:
# obj = pickle.load(file)

# Example: Writing and Reading the State of an Object using the 'pickle' Module
import pickle

class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print(self.eno, "\t", self.ename, "\t", self.esal, "\t", self.eaddr)

# Pickling the Employee object and writing it to a file
with open("emp.dat", "wb") as f:
    e = Employee(100, "Durga", 1000, "Hyd")
    pickle.dump(e, f)
    print("Pickling of Employee Object completed...")

# Unpickling the Employee object from the file and displaying its information
with open("emp.dat", "rb") as f:
    obj = pickle.load(f)
    print("Printing Employee Information after unpickling")
    obj.display()
