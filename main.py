from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

import requests
import threading


# 🌐 URL de tu backend (Render / Railway)
BACKEND_URL = "https://TU_BACKEND.onrender.com/chat"


class UI(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.label = Label(text="Vannia AI lista")
        self.add_widget(self.label)

        self.input = TextInput(hint_text="Escribe algo...")
        self.add_widget(self.input)

        btn = Button(text="Enviar")
        btn.bind(on_press=self.send)
        self.add_widget(btn)

    def send(self, instance):
        text = self.input.text.strip()

        if not text:
            self.label.text = "Escribe algo primero"
            return

        threading.Thread(target=self.call_backend, args=(text,), daemon=True).start()

    def call_backend(self, text):
        try:
            r = requests.post(
                BACKEND_URL,
                json={"text": text},
                timeout=20
            )

            data = r.json()

            self.label.text = data.get("reply", str(data))[:1000]

        except Exception as e:
            self.label.text = f"Error: {str(e)}"


class VanniaApp(App):
    def build(self):
        return UI()


if __name__ == "__main__":
    VanniaApp().run()
