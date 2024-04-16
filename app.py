from flask import Flask, jsonify, request, funcoes # type: ignore

app = Flask(__name__)

@app.route("/", methods=("GET",))
def index():
    return jsonify({"status": 200, "message": "API Larissa helena"})

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

@app.route("/salario", methods = ("GET",))
def salario():
    from random_data import pessoas
    import funcoes
    num = funcoes.mais_2000(pessoas)
    return jsonify( {"status": 200, "data": num} )

@app.route("/maiores_salarios", methods = ("GET",))
def dados():
    from random_data import pessoas
    import funcoes
    num = funcoes.maior_salario(pessoas)
    return jsonify( {"status": 200, "data": num} )

@app.route("/salario_media", methods = ("GET",))
def media_salarial():
    from random_data import pessoas
    import funcoes
    num = funcoes.media_profissoes(pessoas)
    return jsonify( {"status": 200, "data": num} )

@app.route("/salario_idade", methods = ("GET",))
def intervalo():
    from random_data import pessoas
    import funcoes
    num = funcoes.maior_2000_sexo(pessoas)
    return jsonify( {"status": 200, "data": num} )

if __name__ == 'main':
    app.run(debug=True)