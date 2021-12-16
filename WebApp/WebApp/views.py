from WebApp import app
from flask import render_template, request

"""
This is a webapp made with flask framework.

Routes:
    / - shows index.html
    /api/<var> - shows api.html
    /login - shows login.html
"""

@app.route("/")
def home_route():
    """
    This is the standard route for application.
    When user connects with root adress ("/"),
    The application will serve the index.html file
    in response.

    Routes:
        / - renders index.html
    
    Returns:
        Rendered flask template
    """
    return render_template("index.html")

@app.route("/api/<var>")
def api_route(var):
    """
    When user connects with /api/ route, the
    site will print the "api.html" site template
    using the given <var> value.

    Args:
        var (str): The parameter given by api call 
    
    Routes:
        /api/<var> - renders api.html with the given <var> parameter

    Returns:
        Rendered flask template
    """
    return render_template("api.html", var=var)

@app.route("/login", methods=["GET", "POST"])
def login_route():
    """
    This function renders the "login.html" which
    is a simple login form. After sending login information
    using the "log in" button it will display the received information.

    Routes:
        /login - renders login.html

    HTTPMethods:
        GET - used to render the site
        POST - used to send login info from site to backend

    Returns:
        Rendered flask template
    """
    state = "Unauthenticated"
    if request.method == "POST":
        login = request.form["login"]
        password = request.form["password"]
        state = f"{state} {login}:{password}"
    return render_template("login.html", state=state)


               


  


               

               

               

               


    