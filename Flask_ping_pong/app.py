import flask

app = flask.Flask(__name__)


@app.route('/')
def ping():
    return {'message': 'pong'}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
