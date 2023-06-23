from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '4fa8fdaf59fcb947808e183c48fcda81'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
app.app_context().push()

from comunidadeImpressionadora import routes








