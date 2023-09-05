# Import the json module to work with JSON data
import json

# Define a custom Employee class
class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print('ENO:{}, ENAME:{}, ESAL:{}, EADDR:{}'.format(self.eno, self.ename, self.esal, self.eaddr))

# Create an Employee object
e = Employee(100, 'Durga', 1000.0, 'Hyderabad')

# Serialize the Employee object to a JSON file
with open('emp.json', 'w') as f:
    json.dump(e.__dict__, f, indent=4)

# Deserialize the JSON file back into an Employee object
with open('emp.json', 'r') as f:
    edict = json.load(f)

# Create a new Employee object from the deserialized data
newE = Employee(edict['eno'], edict['ename'], edict['esal'], edict['eaddr'])

# Display the details of the new Employee object
newE.display()
