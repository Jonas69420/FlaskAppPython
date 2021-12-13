from flask import Blueprint, render_template
import json
import main

views = Blueprint('views', __name__)

def load_clicks():
  with open('./clicker.json', 'r') as file:
    data = json.load(file)

    for i in data['clicker']:
      if i['clicks']:
        return i['clicks']

  return 0

def set_clicks(value):
  with open('./clicker.json', 'r+') as file:
    data = json.load(file)

    for i in data['clicker']:
      if i['clicks']:
        i['clicks'] += value
        break

    file.seek(0)
    json.dump(data, file, indent = 2)

@views.route('/')
def home_page():
    set_clicks(1)
    main.isHome = True
    return render_template("home.html", clicks=load_clicks())