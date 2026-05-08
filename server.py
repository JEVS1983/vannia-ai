from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# API KEY desde Render Environment Variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Modelo Gemini corregido
GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    f"gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
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
                "reply": "No se recibieron datos"
            })

        text = data.get("text", "")

        if text.strip() == "":
            return jsonify({
                "reply": "Mensaje vacío"
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

        # Validación segura
        if "candidates" not in result:
            return jsonify({
                "reply": f"Error Gemini: {result}"
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
