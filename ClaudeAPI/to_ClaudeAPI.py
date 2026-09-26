from flask import Flask, render_template, request, redirect, jsonify
import anthropic as ap
import requests
import os

app = Flask(__name__)

@app.route("/to_claude", methods = ["POST","GET"])
def to_claude():
    data = request.get_json()
    print(data)

    client = ap.Anthropic(
        api_key = os.environ.get("ANTHOROPIC_API_KEY")
    )

    message = client.messages.create(
        model = "claude-opus-5",
        max_tokens=1024,
        messages = [
            {"role": "user", "content": "以下の四つを基準として理解してください。\n theoly : １．SDTを基準に自立スタイルを促す。２．ポジティブフレーミングを行う。３．自己効力感、有能感、自律性を損なわない。４．元のテキストの内容は変更しない。"},
            {"role": "assistant", "content": "理解しました。"},
            {"role": "user", "content": f"あなたが今理解した基準に沿って以下のtextを言い換えてください。\n text: {data}"}
        ]
    )

    output = message.content[2].text

    return jsonify(
        output
    )