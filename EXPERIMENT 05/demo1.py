from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "HELLO WORLD"

@app.route("/home")
def home():
    return "HELLO HOME PAGE"

app.run(port=5000)
