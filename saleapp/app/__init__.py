from flask import Flask
from urllib .parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)

app.secret_key = 'UYVFYVFYYYFKL@#$G7$^JJNJ((&^^^'
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" % quote('Mai2004@')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8

db = SQLAlchemy(app=app)
login =  LoginManager(app=app)

cloudinary.config(
    cloud_name = "dglrht3fj",
    api_key = "967522359525179",
    api_secret = "L2Pupa5YpllB4M4B-m2dsw9PcSw", # Click 'View API Keys' above to copy your API secret
    secure=True
)
