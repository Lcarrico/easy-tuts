import json
import logging

data = {
    "name": "Leo",
    "age": 27,
    "friends": {'Bob', 'Alice', 'Jill'}
}

json_string = json.dumps(data, indent=2)

# Has something that looks like json data, ex. {"name":"Person"} then turn it into python dict like this
parsed_dat = json.loads(json_string)


# write json to file
with open('jsonfile.json', 'w') as file:
    json.dump(data, file)

# read json from file
with open('jsonfile.json', 'r') as file:
    data = json.load(file)


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, str):
            return obj.lower()
        if isinstance(obj, int):
            return str(obj)
        if isinstance(obj, set):
            return list(obj)
        
        return super().default(obj)
    

custom_json_string = json.dumps(data, cls=CustomEncoder)

print(custom_json_string)



try:
    json_response = {'name':12}
    if not isinstance(json_response['name'], str):
        raise TypeError("name from json is incorrect type")

except TypeError as err:
    logging.exception(err)


class Box():
    num_of_sides=5
    side_length=10

    def function():
        pass

# GraphQL => still in it's evolving phases
        # supposed an ideal replacement for REST APIs, that focuses on JSON calls
    
#http post 'https://example.com/users'
    # {
    #     username
    #     number_followers
    # }
