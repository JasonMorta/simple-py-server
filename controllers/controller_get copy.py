from aiohttp import web


# get request to send a message
async def get_req(request):
    data = {'message': 'Hello, world!'}
    
    # response to server with json data
    return web.json_response(data)