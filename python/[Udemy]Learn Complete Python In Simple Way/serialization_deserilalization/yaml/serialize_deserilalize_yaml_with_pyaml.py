# Import the yaml module from the pyaml library
from pyaml import yaml

# Create a Python dictionary
emp_dict = {'name': 'Durga', 'age': 35, 'salary': 1000.0, 'isMarried': True}

# Serialization to a YAML string
yaml_string = yaml.dump(emp_dict)
print("Serialized to YAML string:")
print(yaml_string)

# Serialization to a YAML file
with open('emp.yaml', 'w') as f:
    yaml.dump(emp_dict, f)
print("Serialized to YAML file (emp.yaml)")

# Deserialization from a YAML string
ed = yaml.safe_load(yaml_string)
print("\nDeserialized from YAML string:")
print(ed)
for k, v in ed.items():
    print(k, ':', v)

# Deserialization from a YAML file
with open('emp.yaml', 'r') as f:
    edf = yaml.safe_load(f)
print("\nDeserialized from YAML file:")
print(edf)
