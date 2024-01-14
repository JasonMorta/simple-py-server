from aiohttp import web
from middleware.make_token import create_jwt_token

# Login function


async def login(request):
    print(request)
    try:
        # Assuming the data is sent in the request body as JSON
        data = await request.json()
        print(data)
        # Get the username and password from the request body
        email = data.get('email')
        password = data.get('password')
        remember = data.get('remember')

        # ============================================================
        # Call a function to check if user exists in database
        # ============================================================

        # Check if username is included
        if email:

            # Configure session and cookie settings
            session_config = {
                'max_age': 3600,  # Session timeout in seconds (e.g., 1 hour)
                'httpOnly': True,  # Set the httpOnly flag for security
            }

            # If correct, return a JWT
            token = create_jwt_token(email)

            # Create a response
            # Also include basic user info
            response = web.json_response({
                'message': 'Successfully logged in',
                'token': token,
            })

            # Set the cookie in the response
            # Set the cookie in the response
            response.cookies['login_cookie'] = token
            response.cookies['login_cookie']['max-age'] = 3600 # expire in 1 hour
            response.cookies['login_cookie']['httponly'] = True  # Set httponly here

            return response
        else:
            # If not correct, return an error
            return web.json_response({'error': 'Invalid username or password'})
    except Exception as e:
        print(e)
        return web.json_response({'error': 'Error logging in'})
