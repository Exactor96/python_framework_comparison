from japronto import Application


def ping(request):
    return request.Response(json={'message': 'pong'})


app = Application()
app.router.add_route('/', ping)
app.run(debug=False, worker_num=8)
