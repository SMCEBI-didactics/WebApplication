from WebApp import app
from flask import render_template, request

"""
"""

@app.route("/")
def home_route():
    """Function that renders home template - index.html.

    Returns:
        str: rendered template.
    """
    return render_template("index.html")

@app.route("/api/<var>")
def api_route(var):
    """Function that renders api template.

    Args:
        var (str): parameter for context argument.

    Returns:
        str: rendered template.
    """
    return render_template("api.html", var=var)

@app.route("/login", methods=["GET", "POST"])
def login_route():
    """Function that renders login template.

    Returns:
        str: rendered template.
    """
    state = "Unauthenticated"
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]
        state = f"{state} {login}:{password}"
    return render_template("login.html", state=state)


               


  


               

               

               

               
