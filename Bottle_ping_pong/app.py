from bottle import route, run


@route('/')
def index():
    return {'message': 'pong'}


if __name__ == '__main__':
    run(server='gunicorn', workers=8, host='localhost', port=5000)
