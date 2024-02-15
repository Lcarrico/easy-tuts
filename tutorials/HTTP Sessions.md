## Python Requests and Session Tutorial

### Introduction
The `requests` library in Python simplifies the process of making HTTP requests. Sessions provide a way to persist parameters across requests, such as cookies. This tutorial will guide you through the basics of making HTTP requests and using sessions in Python.

### Installing Requests
Before you start, make sure you have the `requests` library installed. If not, you can install it using:

```bash
pip install requests
```

### Making a POST Request with Sessions

```python
import requests
import sys

# Creating a session for persistent parameters (e.g., cookies)
session = requests.Session()

# Login payload for POST request
login_payload = {'username': 'username', 'password': 'password'}
login_url = 'https://example.com/login'

# Logging in with a POST request using the session
response = session.post(login_url, data=login_payload)

# Checking if login was successful
if response.ok:
    print("Login successful")
else:
    print("ERROR LOGGING IN")
    sys.exit()
```

In this section, a session is created using `requests.Session()`. Sessions are used to persist parameters like cookies across multiple requests. This is particularly useful for maintaining a stateful connection with a web server.

### Making a GET Request with a Session

```python
# URL for a protected resource
protected_url = 'https://example.com/protected/resource'

# Accessing a protected resource with a GET request using the session
protected_response = session.get(protected_url)

# Checking if access to the protected resource was successful
if protected_response.ok:
    # Perform logic here for the protected resource
    pass
else:
    print("ERROR ACCESSING PROTECTED RESOURCE")
    sys.exit()
```

Sessions automatically persist cookies across requests. In this section, a GET request is made to a protected resource using the session, and the cookies from the login session are included.

### Extracting Cookies from a Session

```python
# Extracting cookies from the session
cookies = session.cookies

# Creating a new session for a different domain
sf_session = requests.Session()

# Accessing a resource on a different domain
sf_url = 'https://snowflake.com/users'
sf_response = sf_session.get(sf_url)

# Closing the original session
session.close()
```

Sessions store cookies in the `session.cookies` attribute. In this section, cookies are extracted from the original session, and a new session is created for a different domain (`snowflake.com`). This demonstrates the ability to use separate sessions for different purposes.

