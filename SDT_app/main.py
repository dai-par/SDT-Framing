from flask import Flask, render_template

app = Flask(__name__)

from SDT_app import main


@app.route("/")
def index():
    return render_template(
        "index.html"
    )