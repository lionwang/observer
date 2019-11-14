__version__ = '0.1.0'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1:3306/observer?charset=utf8' # mysql://username:password@hostname/database
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True #这里是个很有趣的地方

db = SQLAlchemy(app)

from observer.api.users import controllers

