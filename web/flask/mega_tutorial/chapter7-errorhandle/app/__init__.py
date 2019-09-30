from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login.login_manager import LoginManager
from app.log import logging_module

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'afjah3ur38thgh'
login = LoginManager(app)
login.login_view = 'login'

# 日志
app.logger = logging_module.getLogger('log/log.log', 'mylog')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

