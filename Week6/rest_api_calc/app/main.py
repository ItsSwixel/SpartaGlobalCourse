from flask import Flask, make_response, request, render_template, redirect
import jwt
import datetime
import sqlite3
from contextlib import closing
import hashlib
from calc_package import calc_module

SECRET_KEY = "E122B47F25FDA46567B5E88AC42F4"
flask_app = Flask(__name__)


def create_token(username):
    validity = datetime.datetime.utcnow() + datetime.timedelta(days=15)
    token = jwt.encode({'username': username, 'expiry': str(validity)}, SECRET_KEY, "HS256")
    return token


def verify_token(token):
    if token:
        decoded_token = jwt.decode(token, SECRET_KEY, "HS256")
        print(decoded_token)
        with closing(sqlite3.connect("data.db")) as conn:
            with closing(conn.cursor()) as cursor:
                cursor.execute("SELECT * FROM users WHERE username = ? AND token = ?;",
                               (decoded_token['username'], token,))
                data = cursor.fetchall()
                if len(data) == 0:
                    return False
                else:
                    return True


@flask_app.route('/calc')
def calc_page():
    isUserLoggedIn = False
    if 'token' in request.cookies:
        isUserLoggedIn = verify_token(request.cookies['token'])
    if isUserLoggedIn:
        decoded_token = jwt.decode(request.cookies['token'], SECRET_KEY, "HS256")
        username = decoded_token['username']
        return render_template('calc.html', value=f"Welcome {username}!")
    else:
        return redirect("https://127.0.0.1:5000/")


@flask_app.route('/calculate', methods=['POST'])
def calculator():
    num1 = int(request.form['number1'])
    num2 = int(request.form['number2'])
    add = calc_module.addition(num1, num2)
    sub = calc_module.subtraction(num1, num2)
    mul = calc_module.multiplication(num1, num2)
    div = calc_module.division(num1, num2)
    return render_template('calc.html', addi=f"Addition: {add}", subt=f"Subtraction: {sub}",
                           mult=f"Multiplication: {mul}", divi=f"Division: {div}")


@flask_app.route('/')
def splash_page():
    return render_template('splash_page.html')


@flask_app.route('/login')
def login_page():
    isUserLoggedIn = False
    if 'token' in request.cookies:
        isUserLoggedIn = verify_token(request.cookies['token'])
    if isUserLoggedIn:
        return redirect('https://127.0.0.1:5000/calc')
    else:
        return render_template('login.html')


@flask_app.route('/authenticate', methods=['POST'])
def authenticate_users():
    data = request.form
    username = data['username']
    password = data['password']
    password = hashlib.sha256(password.encode()).hexdigest()
    with closing(sqlite3.connect("data.db")) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, token TEXT);")
            conn.commit()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?;", (username, password,))
            rows = cursor.fetchall()
            if len(rows) == 0:
                cursor.execute(f"INSERT INTO users (username, password) VALUES (?, ?);", (username, password))
                conn.commit()
                user_token = create_token(username)
                cursor.execute("UPDATE users SET token = ? WHERE username = ? AND password = ?;",
                               (user_token, username, password,))
                conn.commit()
                resp = make_response(redirect('https://127.0.0.1:5000/calc'))
                resp.set_cookie('token', user_token)
                return resp
            else:
                user_token = create_token(username)
                cursor.execute("UPDATE users SET token = ? WHERE username = ? AND password = ?;",
                               (user_token, username, password,))
                conn.commit()
                resp = make_response(redirect('https://127.0.0.1:5000/calc'))
                resp.set_cookie('token', user_token)
                return resp


if __name__ == '__main__':
    print("This is a REST API Calculator")
    flask_app.run(debug=True, ssl_context=('certs/cert.pem', 'certs/key.pem'))
