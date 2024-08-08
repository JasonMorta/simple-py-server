A simple python sever, thats uses aiohttp.

- Files are mobilized, and the server is run from the server.py file.
- Container controller with simle logic to handle the requests.
- Routes have all HTTP request methods, and are handled by the controllers.
- Middleware are place on all routes, and are used to log the requests going through the server and checks for an API key in the headers of each request.


### Installation
- Install aiohttp and cors
```sh
pip install aiohttp aiohttp_middlewares

```

- Start the server
```sh   
python server.py
```



On render hosting platform. Commands to run the server are as follows:
Build Command: pip install -r requirements.txt
Start Command: python server.py