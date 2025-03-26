from flask import Flask
from flask_pymongo import PyMongo
from routes import produtos_bp
import config
from db import app, mongo

app = Flask(__name__)
app.config["MONGO_URI"] = config.MONGO_URI
mongo = PyMongo(app)

# Registrar blueprint das rotas
app.register_blueprint(produtos_bp, url_prefix="/produtos")

if __name__ == "__main__":
    app.run(debug=True)
