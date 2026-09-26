from flask import Flask, redirect, request, jsonify
import requests
import anthropic as ap
import os

app = Flask(__name__)

@app.route("/evaluate", methods = ["POST"])
def evaluate():
    translate_data = request.form.get("output")

    client = ap.Anthropic(
        api_key = os.environ.get("ANTHOROPIC_API_KEY")
    )
    message = client.messages.create(
            model = "claude-opus-5",
        max_tokens=1024,
        messages = [
            {"role": "user", "content": "以下の四つを基準として理解してください。\n theoly : １．SDTを基準に自立スタイルを促す。２．ポジティブフレーミングを行う。３．自己効力感、有能感、自律性を損なわない。４．元のテキストの内容は変更しない。※出力は何パーセントのみ"},
            {"role": "assistant", "content": "理解しました。"},
            {"role": "user", "content": f"あなたが今理解した基準に沿って以下のtextが基準に沿っているかを評価して適正度を％で表してください。\n text: {translate_data}"}
        ]
    )

    print(message.content[1].text)
    evaluate_output = message.content[1].text
    

    return jsonify(evaluate_output)