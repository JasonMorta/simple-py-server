# Import necessary modules from the http.server module
from http.server import BaseHTTPRequestHandler, HTTPServer

# Set the host and port for the server
HOST = 'localhost'
PORT = 8080

# Define a custom class MyServer that inherits from BaseHTTPRequestHandler
class MyServer(BaseHTTPRequestHandler):
    
    # Override the do_GET method to handle GET requests
    def do_GET(self):
        # Check if the requested path is '/'
        if self.path == '/':
            # Redirect '/' to '/index.html'
            self.path = '/index.html'
            
        try:
            # Attempt to open the requested file and read its content
            file_to_open = open(self.path[1:]).read()
            # Send a success response (HTTP 200 OK)
            self.send_response(200)
        except:
            # If the file is not found, set a custom error message
            file_to_open = 'File not found'
            # Send a not found response (HTTP 404 Not Found)
            self.send_response(404)
            # End the HTTP headers
            self.end_headers()
            # Write the error message to the response body
            self.wfile.write(bytes(file_to_open, 'utf-8'))       

# Create an instance of HTTPServer with the specified host, port, and custom request handler (MyServer)
httpd = HTTPServer((HOST, PORT), MyServer)

# Print a message indicating that the server is running
print("Server running on port", PORT)

# Start the server and keep it running indefinitely
httpd.serve_forever()
