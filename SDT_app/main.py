from flask import Flask, render_template, request, redirect, jsonify
import requests

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.json.ensure_ascii = False

@app.route("/")
def index():
    return render_template(
        "index.html"
    )

@app.route("/upload", methods=["POST"])
def upload():
    message = request.form.get("message")

    response = requests.post(
        "http://127.0.0.1:5001/to_claude",
        json = {"message": message})

    output = response.json()

    return render_template(
        "index.html",
        output = output
    )
