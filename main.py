from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return"<p>Hello, World</p>"

@app.route("/teste")
def rota_teste():
    return"<p>Rota_teste!</p>"