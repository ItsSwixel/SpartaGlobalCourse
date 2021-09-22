from flask import Flask

flask_app = Flask(__name__)


@flask_app.route('/')
def index_page():
    return "This is the index page of a Secure REST API"


@flask_app.route('/help')
def help_page():
    return "This is the help page"


if __name__ == '__main__':
    print("This is a Secure REST API Server")
    flask_app.run(debug=True, ssl_context=('cert/cert.pem', 'cert/key.pem'))
