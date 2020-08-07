from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/connection", methods=["POST", "GET"])
def connection():
    name = request.form.get("name")
    print(name)
    return render_template("connection.html")
