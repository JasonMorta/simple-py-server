# Middleware function
def jwt_middleware():
    # Extract the token from the Authorization header
    token = request.headers.get('Authorization', '').split('Bearer ')[-1]

    try:
        # Decode the token
        decoded_payload = createToken.decode(token, secret, algorithms=['HS256'])

        # Attach the decoded payload to the Flask request context (g)
        g.jwt_payload = decoded_payload

    except createToken.ExpiredSignatureError:
        abort(401, 'Token has expired')

    except createToken.InvalidTokenError:
        abort(401, 'Invalid token')

    # Return the middleware function
    return jwt_middleware


# Export the middleware function
create_jwt_token = create_jwt_token()