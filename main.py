```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

import requests
import threading

SERVER_URL = "https://vannia-ai.onrender.com/chat"


class ChatLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=10, padding=10, **kwargs)

        self.output = Label(
            text="Vannia AI lista",
            size_hint=(1, 0.8)
        )

        self.input = TextInput(
            hint_text="Escribe un mensaje",
            multiline=False,
            size_hint=(1, 0.1)
        )

        self.button = Button(
            text="Enviar",
            size_hint=(1, 0.1)
        )

        self.button.bind(on_press=self.send_message)

        self.add_widget(self.output)
        self.add_widget(self.input)
        self.add_widget(self.button)

    def send_message(self, instance):
        text = self.input.text.strip()

        if text == "":
            return

        self.output.text = "Pensando..."
        self.input.text = ""

        threading.Thread(
            target=self.ask_ai,
            args=(text,),
            daemon=True
        ).start()

    def ask_ai(self, text):

        try:
            response = requests.post(
                SERVER_URL,
                json={"text": text},
                timeout=60
            )

            data = response.json()

            if "reply" in data:
                result = data["reply"]

            elif "error" in data:
                result = "Error: " + str(data["error"])

            else:
                result = "Respuesta inválida"

        except Exception as e:
            result = "Error conexión: " + str(e)

        Clock.schedule_once(lambda dt: self.update_label(result))

    def update_label(self, text):
        self.output.text = text


class VanniaApp(App):

    def build(self):
        return ChatLayout()


if __name__ == "__main__":
    VanniaApp().run()
```
