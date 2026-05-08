from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# API KEY desde Render
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# URL correcta Gemini
GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    f"gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
)


@app.route("/")
def home():
    return "Vannia AI server online"


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "reply": "No data received"
            })

        text = data.get("text", "").strip()

        if not text:
            return jsonify({
                "reply": "Empty message"
            })

        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": text
                        }
                    ]
                }
            ]
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(
            GEMINI_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        result = response.json()

        print(result)

        # Manejo de errores Gemini
        if "error" in result:
            return jsonify({
                "reply": f"Error Gemini: {result['error']['message']}"
            })

        # Validar candidates
        if "candidates" not in result:
            return jsonify({
                "reply": f"Unexpected response: {result}"
            })

        reply = (
            result["candidates"][0]
            ["content"]["parts"][0]["text"]
        )

        return jsonify({
            "reply": reply
        })

    except Exception as e:
        return jsonify({
            "reply": f"Server error: {str(e)}"
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
