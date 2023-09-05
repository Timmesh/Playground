# Import the json module
import json

# Define a Python dictionary object
employee = {
    'name': 'durga',
    'age': 35,
    'salary': 1000.0,
    'ismarried': True,
    'ishavinggirlfriend': None
}

# Serialize the Python dictionary to a JSON string using dumps()
json_string = json.dumps(employee, indent=4, sort_keys=True)

# Print the serialized JSON string
print(json_string)

# Open a JSON file for writing using a context manager
with open('emp.json', 'w') as f:
    # Serialize and write the Python dictionary to the JSON file using dump()
    json.dump(employee, f, indent=4)
