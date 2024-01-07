from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = "SDASFAKIGSDKIDCVSDDF"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sql"

db = SQLAlchemy(app)
login_manager=LoginManager(app)
login_manager.login_view="OR"