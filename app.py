from flask import Flask, render_template

# Flask é um mine-framework (gerencia rotas)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

from api import bp
app.register_blueprint(bp)

if __name__ == "_main_":
    app.run(host="0.0.0.0")