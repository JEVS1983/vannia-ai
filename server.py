from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# API KEY
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# URL API
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

# Memoria simple
conversation_history = []


@app.route("/")
def home():
    return "Vannia AI online"


@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history

    try:
        data = request.get_json()

        if not data:
            return jsonify({"reply": "No se recibieron datos"})

        text = data.get("text", "").strip()

        if not text:
            return jsonify({"reply": "Mensaje vacío"})

        # PERSONALIDAD VANNIA
        system_prompt = {
            "role": "system",
            "content": (
                "Tu nombre es Vannia AI. "
                "Eres una asistente inteligente, amable, emocional y moderna. "
                "Responde SIEMPRE en español. "
                "Habla de forma natural y amigable. "
                "No digas que eres una IA de OpenAI ni Groq. "
                "Tus respuestas deben sentirse humanas y cercanas."
            )
        }

        # guardar memoria
        conversation_history.append({
            "role": "user",
            "content": text
        })

        # limitar memoria
        if len(conversation_history) > 10:
            conversation_history = conversation_history[-10:]

        messages = [system_prompt] + conversation_history

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": messages,
            "temperature": 0.8,
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

        if "error" in result:
            return jsonify({
                "reply": f"Error: {result['error']}"
            })

        reply = result["choices"][0]["message"]["content"]

        # guardar respuesta IA
        conversation_history.append({
            "role": "assistant",
            "content": reply
        })

        return jsonify({
            "reply": reply
        })

    except Exception as e:
        return jsonify({
            "reply": f"Server error: {str(e)}"
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
