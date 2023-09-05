# Import the json module
import json

# Open the JSON file 'emp.json' for reading ('r' mode)
with open('emp.json', 'r') as f:
    # Deserialize the JSON data from the file into a Python dictionary using json.load()
    emp_dict = json.load(f)

# Print the type of emp_dict (it should be a dictionary)
print(type(emp_dict))

# Access and print individual fields from the deserialized dictionary
print('Employee Name:', emp_dict['name'])
print('Employee Age:', emp_dict['age'])
print('Employee Salary:', emp_dict['salary'])
print('Is Employee Married:', emp_dict['ismarried'])
print('Is Employee Has GF:', emp_dict['ishavinggirlfriend'])

# Loop through the dictionary items and print key-value pairs
for k, v in emp_dict.items():
    print('{} : {}'.format(k, v))
