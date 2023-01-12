from WebApp import app
from flask import render_template, request

"""
"""

@app.route("/")
def home_route():
    """
    Strona główna
    """
    return render_template("home.html")









