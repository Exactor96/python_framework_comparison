from aiohttp import web


async def ping(request):
    return web.json_response({'message': 'pong'})


app = web.Application()
app.add_routes([web.get('/', ping)])
