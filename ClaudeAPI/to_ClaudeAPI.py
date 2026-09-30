from flask import Flask, request, jsonify
import anthropic as ap
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
            {"role": "user", "content": "以下の5つを基準として理解してください。\n theoly : １．SDTを基準に自立スタイルを促す。２．ポジティブフレーミングを行う。３．自己効力感、有能感、自律性を損なわない。４．元のテキストの内容は変更しない。５．言葉調も敬語なら敬語。タメ口ならタメ口で揃えてください※出力内容に含めていいのは言い換え分のみです。"},
            {"role": "assistant", "content": "理解しました。"},
            {"role": "user", "content": f"あなたが今理解した基準に沿って以下のtextを言い換えてください。\n text: {data}"}
        ]
    )
    print(message.content[1].text)

    output = message.content[1].text

    return jsonify(output)