from aiohttp import web
import aiohttp_cors  # Import aiohttp_cors

from routes.login_route import login

# Function to set up CORS middleware
async def setup_cors(app):
    # Enable CORS for all routes
    cors = aiohttp_cors.setup(app, defaults={
        # Configure CORS for all routes with default options
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,  # Allow sending credentials (e.g., cookies) with requests
            expose_headers="*",       # Expose all headers to the client
            allow_headers="*",        # Allow all headers in requests
        )
    })

    # Add CORS to each route in the app
    for route in list(app.router.routes()):
        cors.add(route)

# Create an instance of the web application
app = web.Application()

# Add the CORS setup function to the app's startup process
app.on_startup.append(setup_cors)

# Define a login route
app.router.add_route('POST', '/login', login)

# Run the web application on port 8080
web.run_app(app, port=8080)
