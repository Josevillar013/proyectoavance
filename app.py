from flask import Flask, render_template, request
from nlp_utils import limpiar_texto
from responses import obtener_respuesta

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    respuesta = ""
    if request.method == "POST":
        entrada = request.form["mensaje"]
        tokens = limpiar_texto(entrada)
        respuesta = obtener_respuesta(tokens)
        return render_template("index.html", respuesta=respuesta, mensaje=entrada)
    return render_template("index.html", respuesta=respuesta)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
