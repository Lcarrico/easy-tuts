import requests
import sys


session = requests.Session()

login_payload = {
    'username':'username',
    'password':'password'
}

url = 'https://example.com/login'
response = session.post(url, data=login_payload)


url = 'https://example.com/protected/resource'
protected_response = session.get(url)


if protected_response.ok:
    # do logic here
    pass
else:
    print("ERROR LOGGING IN")
    sys.exit()



cookies = session.cookies
sf_session = requests.Session()

# url = 'snowflake.com'
# response = sf_session.get(url + '/users')

session.close()





