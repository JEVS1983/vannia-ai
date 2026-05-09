from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# API KEY Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# URL Groq
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


@app.route("/")
def home():
    return "Vannia AI with Groq online"


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

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {
                    "role": "user",
                    "content": text
                }
            ],
            "temperature": 0.7,
            "max_tokens": 1024
        }

        response = requests.post(
            GROQ_URL,
            headers=headers,
            json=payload,
            timeout=30
        )

        result = response.json()

        print(result)

        # Error API
        if "error" in result:
            return jsonify({
                "reply": f"Groq Error: {result['error']}"
            })

        reply = result["choices"][0]["message"]["content"]

        return jsonify({
            "reply": reply
        })

    except Exception as e:
        return jsonify({
            "reply": f"Server error: {str(e)}"
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
