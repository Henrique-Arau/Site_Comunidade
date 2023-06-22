from flask import Flask, Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '4fa8fdaf59fcb947808e183c48fcda81'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
database = SQLAlchemy(app)
app.app_context().push()
from comunidadeImpressionadora import routes








