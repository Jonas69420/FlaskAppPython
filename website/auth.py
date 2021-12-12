from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login_page():
    return render_template("login.html")

@auth.route('/logout')
def logout_page():
    return "<h1>Logout Test</h1>"

@auth.route('/sign-up')
def sign_up_page():
    return render_template("sign-up.html")
