# here are our routes
from flask import Blueprint, render_template
# set up the blue print for our flask app
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")