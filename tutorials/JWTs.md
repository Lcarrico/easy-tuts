## Python JWT Tutorial

### Introduction
JSON Web Tokens (JWT) are a compact, URL-safe means of representing claims between two parties. Python provides the `jwt` library for working with JWTs. This tutorial will guide you through the basic concepts and usage of the `jwt` library.

### Installing JWT Library
Before you start, make sure you have the `jwt` library installed. If not, you can install it using:

```bash
pip install PyJWT
```

### Encoding JWT

```python
import jwt as jwt_util

# Data to be included in the JWT
data = {'name': 'Leo', 'age': '28'}

# Secret key for encoding the JWT
secret = 'abrakadabra'

# Encoding the JWT
jwt = jwt_util.encode(data, secret)
print("Encoded JWT:", jwt)
```

In this section, we prepare some data and use a secret key to encode a JWT. The secret key is used for both encoding and decoding the JWT.

### Decoding JWT

```python
import jwt as jwt_util

# Secret key for decoding the JWT
secret = 'abrakadabra'

# Decoding the JWT
decoded_jwt = jwt_util.decode(jwt, secret, algorithms=['HS256'])
print("Decoded JWT:", decoded_jwt)
```

In this section, we use the secret key to decode a previously encoded JWT. The algorithm 'HS256' is specified to match the encoding algorithm.

### Handling Decode Errors

```python
import jwt as jwt_util

try:
    # Trying to decode JWT with an incorrect secret
    decoded_jwt = jwt_util.decode(jwt, '12345', algorithms=['HS256'])
    print("Decoded JWT:", decoded_jwt)
except jwt_util.DecodeError as err:
    print("Error:", str(err))
```

It's important to handle decode errors gracefully. In this example, a `DecodeError` is caught when trying to decode a JWT with an incorrect secret.

### RSA Key Details (Theory)

#### RSA Key Generation
RSA (Rivest–Shamir–Adleman) is a widely used asymmetric encryption algorithm for secure data transmission. It uses a pair of keys: a public key for encryption and a private key for decryption.

To use RSA with JWT, you generate a key pair (public and private) and store the public key on the server for verification.

#### Example

1. Generate RSA Key Pair:

```bash
openssl genpkey -algorithm RSA -out private_key.pem
openssl rsa -pubout -in private_key.pem -out public_key.pem
```

2. Store the `private_key.pem` securely on your server and use it for encoding JWT.
3. Share the `public_key.pem` with anyone who needs to verify the JWT signature.

### RSA Example

```python
import jwt as jwt_util

# Load RSA public key for verification
with open('public_key.pem', 'r') as file:
    public_key = file.read()

# Encode JWT using RSA private key
jwt_rsa = jwt_util.encode(data, private_key, algorithm='RS256')
print("Encoded JWT (RSA):", jwt_rsa)

# Decode JWT using RSA public key
decoded_jwt_rsa = jwt_util.decode(jwt_rsa, public_key, algorithms=['RS256'])
print("Decoded JWT (RSA):", decoded_jwt_rsa)
```

In this example, we use RSA keys for encoding and decoding JWT. The public key is used for verification during decoding. This adds an extra layer of security compared to the shared secret approach.
