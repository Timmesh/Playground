# Import the json module
import json

# JSON-formatted string containing employee information
json_string = '''{
    "name": "durga",
    "age": 35,
    "salary": 1000.0,
    "ismarried": true,
    "ishavinggirlfriend": null
}'''

# Deserialize the JSON string to a Python dictionary using loads()
emp_dict = json.loads(json_string)

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
