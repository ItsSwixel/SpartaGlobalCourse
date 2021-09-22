from flask import Flask, make_response, request, render_template
from random import random

flask_app = Flask(__name__)


@flask_app.route('/')
def index_page():
    print(request.cookies)
    if 'user_id' in request.cookies:
        return "Welcome back to the website!"
    else:
        user_id = random()
        print(f"User ID: {user_id}")
        resp = make_response("This is the index page of a Secure REST API")
        resp.set_cookie('user_id', str(user_id))
    return resp


@flask_app.route('/help')
def help_page():
    return "This is the help page"


@flask_app.route('/login')
def login_page():
    return render_template('login.html')


@flask_app.route('/authenticate', methods=["POST"])
def authenticate_users():
    data = request.form
    username = data['username']
    password = data['password']
    # Check whether username and password are correct
    resp = make_response("Logged in successfully")
    resp.set_cookie("loggedIn", 'True')
    return resp


if __name__ == '__main__':
    print("This is a Secure REST API Server")
    flask_app.run(debug=True, ssl_context=('cert/cert.pem', 'cert/key.pem'))
