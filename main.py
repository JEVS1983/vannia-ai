from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock

import requests
import threading


# URL de tu servidor Render
SERVER_URL = "https://vannia-ai.onrender.com/chat"


class ChatUI(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=10, padding=10, **kwargs)

        # Área de chat
        self.scroll = ScrollView(size_hint=(1, 0.9))

        self.chat_layout = GridLayout(
            cols=1,
            spacing=10,
            size_hint_y=None
        )

        self.chat_layout.bind(minimum_height=self.chat_layout.setter("height"))

        self.scroll.add_widget(self.chat_layout)

        self.add_widget(self.scroll)

        # Caja inferior
        bottom = BoxLayout(
            orientation="horizontal",
            size_hint=(1, 0.1),
            spacing=10
        )

        self.input_text = TextInput(
            hint_text="Escribe tu mensaje...",
            multiline=False
        )

        self.send_button = Button(
            text="Enviar",
            size_hint=(0.3, 1)
        )

        self.send_button.bind(on_press=self.send_message)

        bottom.add_widget(self.input_text)
        bottom.add_widget(self.send_button)

        self.add_widget(bottom)

        self.add_message("Vannia", "Hola 💖 Soy Vannia AI")

    def add_message(self, sender, message):

        text = f"{sender}: {message}"

        label = Label(
            text=text,
            size_hint_y=None,
            halign="left",
            valign="middle"
        )

        label.bind(
            width=lambda *x: label.setter("text_size")(label, (label.width, None))
        )

        label.texture_update()

        label.height = label.texture_size[1] + 30

        self.chat_layout.add_widget(label)

        Clock.schedule_once(lambda dt: setattr(self.scroll, 'scroll_y', 0))

    def send_message(self, instance):

        user_text = self.input_text.text.strip()

        if user_text == "":
            return

        self.add_message("Tú", user_text)

        self.input_text.text = ""

        threading.Thread(
            target=self.get_ai_response,
            args=(user_text,),
            daemon=True
        ).start()

    def get_ai_response(self, text):

        try:

            response = requests.post(
                SERVER_URL,
                json={"text": text},
                timeout=30
            )

            data = response.json()

            if "reply" in data:

                ai_text = data["reply"]

            elif "error" in data:

                ai_text = f"Error: {data['error']}"

            else:

                ai_text = "Respuesta no válida del servidor"

        except Exception as e:

            ai_text = f"Error conexión: {str(e)}"

        Clock.schedule_once(
            lambda dt: self.add_message("Vannia", ai_text)
        )


class VanniaApp(App):

    def build(self):
        return ChatUI()


if __name__ == "__main__":
    VanniaApp().run()
