from flask_pymongo import PyMongo
from flask import Flask
import config

app = Flask(__name__)
app.config["MONGO_URI"] = config.MONGO_URI
mongo = PyMongo(app)
