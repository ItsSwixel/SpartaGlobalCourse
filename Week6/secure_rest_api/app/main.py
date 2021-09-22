from flask import Flask, make_response, request
from random import random

flask_app = Flask(__name__)


@flask_app.route('/')
def index_page():
    print(request.cookies)
    if 'user_id' in request.cookies:
        resp = make_response("Welcome back to the website!")
    else:
        user_id = random()
        print(f"User ID: {user_id}")
        resp = make_response("This is the index page of a Secure REST API")
        resp.set_cookie('user_id', str(user_id))
    return resp


@flask_app.route('/help')
def help_page():
    return "This is the help page"


if __name__ == '__main__':
    print("This is a Secure REST API Server")
    flask_app.run(debug=True, ssl_context=('cert/cert.pem', 'cert/key.pem'))
