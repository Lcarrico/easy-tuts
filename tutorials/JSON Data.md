

## Python JSON and Error Handling Tutorial

### Introduction
JSON (JavaScript Object Notation) is a lightweight data interchange format commonly used for data communication between a server and a web application. Python provides the `json` module to work with JSON data. Additionally, we'll cover error handling using the `logging` module.

### Creating and Parsing JSON

```python
import json

# Creating JSON from a Python dictionary
data = {
    "name": "Leo",
    "age": 27,
    "friends": {'Bob', 'Alice', 'Jill'}
}

json_string = json.dumps(data, indent=2)

# Parsing JSON string into a Python dictionary
parsed_data = json.loads(json_string)

print("Original Data:", data)
print("JSON String:", json_string)
print("Parsed Data:", parsed_data)
```

The `json.dumps` method converts a Python dictionary into a JSON-formatted string, and `json.loads` converts a JSON string back into a Python dictionary.

### Writing and Reading JSON to/from File

```python
import json

# Writing JSON to a file
with open('jsonfile.json', 'w') as file:
    json.dump(data, file)

# Reading JSON from a file
with open('jsonfile.json', 'r') as file:
    loaded_data = json.load(file)

print("Data written to file:", data)
print("Data read from file:", loaded_data)
```

The `json.dump` method writes a Python dictionary to a file in JSON format, and `json.load` reads a JSON file into a Python dictionary.

### Custom JSON Encoding

```python
import json

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, str):
            return obj.lower()
        if isinstance(obj, int):
            return str(obj)
        if isinstance(obj, set):
            return list(obj)
        
        return super().default(obj)

# Using custom encoder
custom_json_string = json.dumps(data, cls=CustomEncoder)

print("Custom JSON String:", custom_json_string)
```

By creating a custom encoder class that inherits from `json.JSONEncoder`, you can define custom serialization rules for certain data types.

### Error Handling with JSON

```python
import logging

try:
    json_response = {'name': 12}
    if not isinstance(json_response['name'], str):
        raise TypeError("Name from JSON is incorrect type")

except TypeError as err:
    logging.exception(err)
```

Error handling is crucial when working with JSON data. In this example, a `TypeError` is raised if the 'name' field in the JSON response is not of type string. The `logging` module is used to log the exception details.
