from flask import Flask, redirect
import requests
import anthropic as ap
import os

app = Flask(__name__)

@app.route("/evaluate", methods = ["POST"])
def evaluate():
    respons = requests.get('http://127.0.0.1:5002/to_claude')

    translate_data = respons.json()

    client = ap.Anthropic(
        api_key = os.environ.get("ANTHOROPIC_API_KEY")
    )
    message = client.messages.create(
            model = "claude-opus-5",
        max_tokens=1024,
        messages = [
            {"role": "user", "content": "以下の四つを基準として理解してください。\n theoly : １．SDTを基準に自立スタイルを促す。２．ポジティブフレーミングを行う。３．自己効力感、有能感、自律性を損なわない。４．元のテキストの内容は変更しない。"},
            {"role": "assistant", "content": "理解しました。"},
            {"role": "user", "content": f"あなたが今理解した基準に沿って以下のtextが基準に沿っているかを評価して適正度を％で表してください。\n text: {translate_data}"}
        ]
    )

    evaluate_output = message.content[2].text

    return redirect(
        "index.html",
        evaluate_output = evaluate_output
    )