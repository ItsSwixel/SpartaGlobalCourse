from flask import Flask

flask_app = Flask(__name__)


@flask_app.route('/')
def index():
    return "Welcome to this server, this is the root"


@flask_app.route('/test')
def test():
    return "This is the testing service"


if __name__ == '__main__':
    print("Welcome to REST API Server")
    flask_app.run(host="0.0.0.0")
