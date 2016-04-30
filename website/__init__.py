import flask

from . import server_config

app = flask.Flask(__name__)
app.secret_key = server_config.SERVER_SECRET

from .server import *
