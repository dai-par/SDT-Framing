from flask import Flask, render_template, request, redirect, jsonify
import requests

app = Flask(__name__)



@app.route("/")
def index():
    return render_template(
        "index.html"
    )

@app.route("/upload", methods=["POST"])
def upload():
    message = request.form.get("message")
    data = {"message": message}

    return jsonify(data[0])