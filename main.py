```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window

import threading
import requests

# URL DE RENDER
SERVER_URL = "https://vannia-ai.onrender.com/chat"

Window.clearcolor = (0.08, 0.08, 0.08, 1)


class ChatUI(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)

        self.output = Label(
            text="Vannia AI lista",
            size_hint_y=0.8,
            halign="left",
            valign="top",
            text_size=(Window.width - 40, None),
        )

        self.input = TextInput(
            hint_text="Escribe aquí...",
            multiline=False,
            size_hint_y=0.1
        )

        self.button = Button(
            text="Enviar",
            size_hint_y=0.1
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
            target=self.ask_server,
            args=(text,),
            daemon=True
        ).start()

    def ask_server(self, text):
        try:
            response = requests.post(
                SERVER_URL,
                json={"text": text},
                timeout=60
            )

            data = response.json()

            if "reply" in data:
                reply = data["reply"]
            elif "error" in data:
                reply = "Error: " + str(data["error"])
            else:
                reply = "Respuesta inválida"

        except Exception as e:
            reply = "Error conexión: " + str(e)

        Clock.schedule_once(lambda dt: self.update_reply(reply))

    def update_reply(self, text):
        self.output.text = text


class VanniaApp(App):

    def build(self):
        return ChatUI()


if __name__ == "__main__":
    VanniaApp().run()
```
