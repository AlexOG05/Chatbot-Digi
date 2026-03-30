from flask import Flask, render_template, request

app = Flask("__name__")

@app.route("/", methods=["GET", "POST"])
def home():
    respuesta = ""

    if request.method == "POST":
        mensaje = request.form["mensaje"]

        respuesta = f"IA dijo: {mensaje}"


    return render_template("index.html", respuesta=respuesta)


if __name__ == "__main__":
    app.run(debug=True)