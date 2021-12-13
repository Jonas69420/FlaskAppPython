from flask import Blueprint, render_template
import main

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login_page():
    main.isHome = False
    return render_template("login.html")

@auth.route('/logout')
def logout_page():
    main.isHome = False
    return "<h1>Logout Test</h1>"

@auth.route('/sign-up')
def sign_up_page():
    main.isHome = False
    return render_template("sign-up.html")
