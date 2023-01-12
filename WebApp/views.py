from WebApp import app
from WebApp.models import *
from flask import render_template, request

"""
"""

@app.route("/")
def home_route():
    """
    Strona główna
    """
    return render_template("home.html")









