from flask import Flask, render_template, request, redirect, jsonify
import requests

app = Flask(__name__)


@app.route("/send")
def send_message():
    response = requests.get("http://127.0.0.1:5000/upload")
    data = response.json()