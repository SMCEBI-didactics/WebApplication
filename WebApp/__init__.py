import os
from flask import Flask

app = Flask(__name__,
            instance_relative_config=True,
            static_folder="static",
            static_url_path="")



# routing
from WebApp import views
# struktura bazy 


