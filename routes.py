from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from db import mongo

produtos_bp = Blueprint("produtos", __name__)

# Listar todos os produtos (GET)
@produtos_bp.route("/", methods=["GET"])
def get_produtos():
    produtos = list(mongo.db.produtos.find({}, {"_id": 1, "nome": 1, "fornecedor": 1, "endereco_fornecedor": 1, "quantidade": 1, "endereco": 1, "preco_unitario": 1}))
    for produto in produtos:
        produto["_id"] = str(produto["_id"])  # Converter ObjectId para string
    return jsonify(produtos), 200

# Criar um novo produto (POST)
@produtos_bp.route("/", methods=["POST"])
def add_produto():
    data = request.json
    if not data:
        return jsonify({"error": "Dados inválidos"}), 400

    novo_produto = {
        "nome": data["nome"],
        "fornecedor": data["fornecedor"],
        "endereco_fornecedor": data["endereco_fornecedor"],
        "quantidade": data["quantidade"],
        "endereco": data["endereco"],
        "preco_unitario": data["preco_unitario"]
    }

    result = mongo.db.produtos.insert_one(novo_produto)
    novo_produto["_id"] = str(result.inserted_id)
    return jsonify(novo_produto), 201

# Atualizar um produto por ID (PUT)
@produtos_bp.route("/<string:id>", methods=["PUT"])
def update_produto(id):
    data = request.json
    if not data:
        return jsonify({"error": "Dados inválidos"}), 400

    resultado = mongo.db.produtos.update_one({"_id": ObjectId(id)}, {"$set": data})

    if resultado.matched_count == 0:
        return jsonify({"error": "Produto não encontrado"}), 404

    return jsonify({"message": "Produto atualizado"}), 200

# Deletar um produto por ID (DELETE)
@produtos_bp.route("/<string:id>", methods=["DELETE"])
def delete_produto(id):
    resultado = mongo.db.produtos.delete_one({"_id": ObjectId(id)})

    if resultado.deleted_count == 0:
        return jsonify({"error": "Produto não encontrado"}), 404

    return jsonify({"message": "Produto deletado"}), 200
