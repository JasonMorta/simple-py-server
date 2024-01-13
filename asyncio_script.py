import aiohttp
from aiohttp import web

    # Sample list of food items
food_items = ['Apple', 'Banana', 'Carrot', 'Doughnut', 'Eggplant']

async def get_food_list(request):
    # Return the list as JSON
    return web.json_response({'food_items': food_items})


async def add_food(request):
    # Get the new food item from the request
    data = await request.json()
    new_food_item = data.get('new_food_item')

    # Add the new food item to the list
    food_items.append(new_food_item)

    # Return the updated list as JSON
    return web.json_response({'food_items': food_items})

async def main():
    app = web.Application()

    # Define a route for the /food endpoint
    app.router.add_get('/food', get_food_list)
    
    # Define a route for adding a new food item
    app.router.add_post('/add_food', add_food)

    # Create the server and run it
    runner = aiohttp.web.AppRunner(app)
    await runner.setup()
    site = aiohttp.web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    print("Server started on http://localhost:8080")
    # Keep the application running
    while True:
        await asyncio.sleep(1)  # Pause for 1 second

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
