## Python HTTP and Requests Tutorial

### Introduction
HTTP (Hypertext Transfer Protocol) is the foundation of data communication on the internet. Python provides the `requests` library to simplify the process of making HTTP requests. This tutorial will guide you through the basic concepts and usage of the `requests` library.

### Installing Requests
Before you start, make sure you have the `requests` library installed. If not, you can install it using:

```bash
pip install requests
```

### Making GET Requests

```python
import requests

# Sending a GET request
response = requests.get('https://jsonplaceholder.typicode.com/posts/1', params={'q': 'sampleData'}, headers={'User-Agent': 'Python'})

# Printing the response status code and content
print("Status Code:", response.status_code)
print("Content:", response.text)
```

In this example, we send a GET request to the URL 'https://jsonplaceholder.typicode.com/posts/1', including query parameters ('q': 'sampleData') and a custom User-Agent header.

### Query Parameters

```python
import requests

# Adding query parameters to a GET request
params = {'param1': 'value1', 'param2': 'value2'}
response = requests.get('https://example.com/api/data', params=params)

print("Status Code:", response.status_code)
print("Content:", response.text)
```

You can include query parameters in your GET requests by passing a dictionary to the `params` parameter.

### Making POST Requests

```python
import requests

# Sending a POST request with JSON data
data = {'somedata': 'thedata'}
response = requests.post('https://webhook.site/dab2c3d6-7308-4730-b390-665b61f1195c', json=data)

print("Status Code:", response.status_code)
print("Content:", response.text)
```

To send data in a POST request, you can use the `json` parameter. It automatically sets the 'Content-Type' header to 'application/json'.

### Handling Response

```python
import requests

# Handling response
response = requests.get('https://example.com/api/data')

if response.status_code == 200:
    print("Request successful")
    print("Content:", response.text)
else:
    print("Request failed with status code:", response.status_code)
```

Check the status code to determine if the request was successful. Typically, status code 200 indicates success.

### Headers

```python
import requests

# Adding custom headers to a request
headers = {'User-Agent': 'Custom-User-Agent'}
response = requests.get('https://example.com/api/data', headers=headers)

print("Status Code:", response.status_code)
print("Content:", response.text)
```

You can include custom headers in your requests, such as the 'User-Agent' in this example.

### Additional HTTP Methods

The `requests` library supports other HTTP methods like PUT, UPDATE, DELETE, HEAD, etc. Usage is similar to the examples provided.
