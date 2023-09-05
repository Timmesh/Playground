# Define the Employee class
class Employee:
    # Constructor to initialize employee attributes
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    # Method to display employee information
    def display(self):
        print(self.eno, "\t", self.ename, "\t", self.esal, "\t", self.eaddr)
