from aiohttp import web
import middleware.make_token as make_token



async def add_food(request):
    try:
        item = request.query.get('item')
        print(item)

        # Add the new item to the list
        food_items.append(item)
        return web.json_response(food_items)

    except Exception as e:
        print(e)
        return web.json_response({'error': 'Error adding item'})

app = web.Application()

# Apply the JWT middleware to all routes
#app.middlewares.append(jwt_middleware)

# Define a login route
app.router.add_post('/login', make_token.login(secret_key))

# Define a route for the /food endpoint
app.router.add_get('/food', get_food_list)

# Define a route for adding a new food item
app.router.add_post('/add_food', add_food)

web.run_app(app, port=8080)
