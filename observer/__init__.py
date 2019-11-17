__version__ = '0.1.0'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_object('observer.config')
db = SQLAlchemy(app)
auth = HTTPTokenAuth(scheme='Bearer')
socketio = SocketIO(app)

from observer.utils import auth_util
from observer.api.users import controllers

