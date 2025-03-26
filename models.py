from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    fornecedor = db.Column(db.String(100), nullable=False)
    endereco_fornecedor = db.Column(db.String(200), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    preco_unitario = db.Column(db.Float, nullable=False)

class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Produto
        load_instance = True
