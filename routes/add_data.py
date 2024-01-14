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
