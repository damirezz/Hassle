#This page contains pages that only renders and have no special function
from flask import Blueprint, render_template

idle = Blueprint('idle', __name__)

@idle.route('/')
def homepage():
    title = 'Home Page'
    return render_template('index.html', title=title)

@idle.route('/welcome')
def welcome():
    title = 'Welcome'
    return render_template('welcome.html', title = title)