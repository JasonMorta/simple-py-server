from datetime import datetime, timedelta
import jwt as createToken
from jose import jwt, jwe


# Set the secret key
secret_key = 'my-secret'

def create_jwt_token(email):
    print("creating a token")

    # Set the current time
    current_time = datetime.utcnow()
    issued_at_time = datetime.utcnow()

    # Calculate the expiration time as 1 day from the current time
    # For hours use: timedelta(hours=1)
    expiration_time = current_time + timedelta(days=1)

    # Convert the expiration time to a Unix timestamp
    expiration_timestamp = int(expiration_time.timestamp())

    # Convert the issued_at_time to a Unix timestamp
    issued_at_timestamp = int(issued_at_time.timestamp())


    # ! Still visible in the token
    payload = {
        # Issuer: The entity that issued the JWT (can be any string, here represented by "*").
        "iss": "*",
        # The "subject" claim typically holds a unique identifier for the user or entity associated with the JWT. It can be a username, user ID, or any other identifier chosen by the issuer.
        "sub": "",
        # The "aud" claim holds one or more values that represent the intended recipients of the JWT. These values are often URLs or identifiers associated with specific services or applications.
        "aud": "/",
        # Role: A custom property indicating the role of the user (here, set to "USER").
        "role": "member",
        # Expiration Time: The expiration time after which the JWT should not be accepted (a Unix timestamp, here set to October 22, 2021, 12:00:00 AM UTC).
        "exp": expiration_timestamp,
        # Issued At: The time at which the JWT was issued.
        "iat": issued_at_timestamp,
        # User info: A custom property indicating the user's email address.
        "user_info": {
            "email": email
        }
    }
    
    # Encode JWT token
    token = createToken.encode(payload, secret_key, algorithm='HS256')


    """ 
    In systems where JWTs are used for delegated authentication 
    (e.g., Single Sign-On), the "iat" claim can be used to check 
    whether the token issuance time aligns with the expected 
    authentication flow.
    """

    return token





