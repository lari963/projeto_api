from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=("GET",))
def index():
    return jsonify({"status": 200, "message": "API Rodrigo"})

@app.route("/aleatorios") #decorator de rota
def aleatorios(): #função python 
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a}) # retorno

@app.route("/argumentos/<string:nome>")
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})

@app.route("/argumentos")
def arg_implicito():
    return jsonify({"status": 200, "data": request.args["nome"]})

@app.route("/idades", methods=("GET",))
def idades():
    from random_data import pessoas
    import funcoes 
    num = funcoes.maior_de_50(pessoas)
    return jsonify({"status": 200, "data": num})

