from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = '4fa8fdaf59fcb947808e183c48fcda81'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.app_context().push()

from comunidadeImpressionadora import routes








