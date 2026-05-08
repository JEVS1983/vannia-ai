from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GEMINI_API_KEY = "TU_API_KEY_AQUI"

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    f"gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
)


@app.route("/chat", methods=["POST"])
def chat():
    try:
        text = request.json.get("text", "")

        payload = {
            "contents": [
                {"parts": [{"text": text}]}
            ]
        }

        r = requests.post(GEMINI_URL, json=payload, timeout=20)
        data = r.json()

        reply = data["candidates"][0]["content"]["parts"][0]["text"]

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
