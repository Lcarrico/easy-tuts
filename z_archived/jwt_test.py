import jwt as jwt_util
import os
import base64



token = os.environ['SF_RSA_KEY']
token = base64.decode(token)


data = {'name':'Leo',
        'age':'28'}

secret = 'abrakadabra'


jwt = jwt_util.encode(data, secret)
print(jwt)

decoded_jwt = jwt_util.decode(jwt, secret, algorithms=['RS256'])
print(decoded_jwt)


try:
    decoded_jwt = jwt_util.decode(jwt, '12345', algorithms=['HS256'])
    print(decoded_jwt)
except jwt_util.DecodeError as err:
    print(str(err))
    
