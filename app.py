from flask import Flask, render_template, jsonify, request
import numeros_cidades as nc
import controller.generator as gn

app = Flask(__name__)

@app.route("/")
def inicial():
    return render_template("index.html", numeros=nc.numeros)

@app.route("/cidade", methods=["POST", "GET"])
def buscar_dados_cidade():
    if request.method == "POST":
        cidade = request.form.get("cidade")
        resultado = gn.buscar_dados(cidade)
        
        return jsonify(resultado)

if __name__ == '__main__':
    app.run()