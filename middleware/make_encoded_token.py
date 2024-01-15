from datetime import datetime, timedelta
from jose import jwe, jwk
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Set the secret key (you can keep it if you still need it)
secret_key = 'my-secret'

def create_jwt_token(email):
    # Set the current time
    current_time = datetime.utcnow()
    issued_at_time = datetime.utcnow()

    # Calculate the expiration time as 1 day from the current time
    expiration_time = current_time + timedelta(days=1)

    # Convert the expiration time to a Unix timestamp
    expiration_timestamp = int(expiration_time.timestamp())

    # Convert the issued_at_time to a Unix timestamp
    issued_at_timestamp = int(issued_at_time.timestamp())
    
    # Generate an RSA key pair
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # ! Still visible in the token
    payload = {
        "iss": "*",  # Issuer
        "sub": "",
        "aud": "/",
        "role": "member",
        "exp": expiration_timestamp,
        "iat": issued_at_timestamp,
        "user_info": {
            "email": email
        }
    }
    
    # Extract public key in JWK format
    public_key = private_key.public_key()
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    public_key_jwk = jwk.construct(public_key_bytes, algorithm='RS256', use='enc')

    # Encrypt the payload
    token = jwe.encode(payload, public_key_jwk, algorithm='RSA-OAEP', enc='A256GCM')

    return token
