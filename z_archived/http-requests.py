import requests
# Types of requests: GET, POST, PUT, UPDATE, DELETE, HEAD (asks for specifically only metadata)
# CRUD => Create, Read, Update, Delete

response = requests.get('https://webhook.site/dab2c3d6-7308-4730-b390-665b61f1195c', params={'q':'sampleData'}, headers={'User-Agent':'Python'})

response = requests.post('https://webhook.site/dab2c3d6-7308-4730-b390-665b61f1195c', json={'somedata':'thedata'})


# response.json() # returns the incoming data into a python dictionary
response.text # grabs the data raw

