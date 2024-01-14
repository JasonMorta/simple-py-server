from aiohttp import web

# Sample list of food items
food_items = ['Apple', 'Banana', 'Carrot', 'Doughnut', 'Eggplant']

async def get_food_list(request):
    # Access the decoded JWT payload
    jwt_payload = request.get('jwt_payload', {})

    # Return the list as JSON along with the user info from the JWT payload
    return web.json_response({'food_items': food_items, 'user_info': jwt_payload})
