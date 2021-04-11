from sanic import Sanic
from sanic.response import json

app = Sanic("Ping Pong app")


@app.get("/")
async def hello_world(request):
    return json({'message': 'pong'})
