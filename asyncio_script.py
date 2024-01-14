import aiohttp
from aiohttp import web
import json

    # Sample list of food items
food_items = ['Apple', 'Banana', 'Carrot', 'Doughnut', 'Eggplant']

# Get the list of food items
async def get_food_list(request):
    # Return the list as JSON
    return web.json_response({'food_items': food_items})

# Adding a new food item
async def add_food(request):
    try:
        item = request.query['item']
        print(item)
        
        # Add the new item to the list
        food_items.append(item)
        return web.json_response(food_items)

    except Exception as e:
        print(e)
        return web.json_response({'error': 'Error adding item'})
     


app = web.Application()

# Define a route for the /food endpoint
app.router.add_get('/food', get_food_list)
    
# Define a route for adding a new food item
app.router.add_post('/add_food', add_food)


web.run_app(app, port=8080)