import jwt

# Define a payload containing the data you want to include in the JWT
payload = {"user_id": 1234, "username": "aishu"}

# Define a secret key that will be used to sign the JWT
secret_key = "mysecretkey"

# Encode the JWT using the payload and secret key
jwt_token = jwt.encode(payload, secret_key, algorithm="HS256")

# Print the encoded JWT
print(jwt_token)


# Decode the JWT using the secret key
decoded_token = jwt.decode(jwt_token, secret_key, algorithms=["HS256"])

# Print the decoded JWT
print(decoded_token)