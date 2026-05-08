from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# =====================================
# API KEY
# =====================================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# =====================================
# URL GEMINI
# =====================================
GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    f"gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
)

# =====================================
# HOME
# =====================================
@app.route("/")
def home():

    return "Vannia AI Backend Online"


# =====================================
# CHAT
# =====================================
@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json()

        text = data.get("text", "")

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

        r = requests.post(
            GEMINI_URL,
            json=payload,
            timeout=30
        )

        result = r.json()

        print(result)

        # =====================================
        # VALIDAR ERROR GEMINI
        # =====================================
        if "candidates" not in result:

            return jsonify({
                "error": str(result)
            })

        # =====================================
        # RESPUESTA
        # =====================================
        reply = result["candidates"][0]["content"]["parts"][0]["text"]

        return jsonify({
            "reply": reply
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


# =====================================
# RUN
# =====================================
if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
