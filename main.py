from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.utils import platform
from kivy.metrics import dp
from kivy.properties import StringProperty

import threading
import requests
import json

# Tamaño de ventana para pruebas en PC
if platform != "android":
    Window.size = (420, 760)


class ChatMessage(Label):
    pass


class MainLayout(BoxLayout):

    api_status = StringProperty("Desconectado")

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=10, padding=10, **kwargs)

        self.history = []

        # Header
        self.header = Label(
            text="Vannia AI",
            size_hint_y=None,
            height=dp(50),
            font_size="24sp",
            bold=True
        )
        self.add_widget(self.header)

        # Estado API
        self.status_label = Label(
            text=f"Estado: {self.api_status}",
            size_hint_y=None,
            height=dp(30),
            font_size="14sp"
        )
        self.add_widget(self.status_label)

        # Scroll chat
        self.scroll = ScrollView()

        self.chat_area = BoxLayout(
            orientation="vertical",
            spacing=10,
            size_hint_y=None,
            padding=10
        )

        self.chat_area.bind(
            minimum_height=self.chat_area.setter("height")
        )

        self.scroll.add_widget(self.chat_area)
        self.add_widget(self.scroll)

        # Input layout
        self.input_layout = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(55),
            spacing=10
        )

        self.user_input = TextInput(
            hint_text="Escribe un mensaje...",
            multiline=False
        )

        self.user_input.bind(on_text_validate=self.send_message)

        self.send_btn = Button(
            text="Enviar",
            size_hint_x=None,
            width=dp(100)
        )

        self.send_btn.bind(on_press=self.send_message)

        self.input_layout.add_widget(self.user_input)
        self.input_layout.add_widget(self.send_btn)

        self.add_widget(self.input_layout)

        self.add_message(
            "🤖",
            "Hola, soy Vannia AI. ¿En qué puedo ayudarte?"
        )

        Clock.schedule_once(lambda dt: self.check_connection(), 1)

    def add_message(self, sender, message):

        bubble = Label(
            text=f"{sender} {message}",
            markup=True,
            size_hint_y=None,
            text_size=(Window.width - dp(40), None),
            halign="left",
            valign="middle",
            padding=(10, 10),
            font_size="16sp"
        )

        bubble.bind(
            texture_size=lambda instance, value:
            setattr(instance, "height", value[1] + 20)
        )

        self.chat_area.add_widget(bubble)

        Clock.schedule_once(
            lambda dt: setattr(
                self.scroll,
                "scroll_y",
                0
            ),
            0.1
        )

    def send_message(self, instance):

        text = self.user_input.text.strip()

        if not text:
            return

        self.add_message("🧑", text)

        self.history.append({
            "role": "user",
            "content": text
        })

        self.user_input.text = ""

        threading.Thread(
            target=self.generate_response,
            args=(text,),
            daemon=True
        ).start()

    def generate_response(self, text):

        try:
            # RESPUESTA LOCAL SIMPLE
            response = self.local_ai_response(text)

            Clock.schedule_once(
                lambda dt: self.add_message("🤖", response)
            )

        except Exception as e:

            Clock.schedule_once(
                lambda dt: self.show_error(str(e))
            )

    def local_ai_response(self, text):

        lower = text.lower()

        if "hola" in lower:
            return "Hola 👋 ¿Cómo estás?"

        elif "nombre" in lower:
            return "Soy Vannia AI."

        elif "hora" in lower:
            from datetime import datetime
            return f"La hora actual es {datetime.now().strftime('%H:%M:%S')}"

        elif "fecha" in lower:
            from datetime import datetime
            return f"Hoy es {datetime.now().strftime('%d/%m/%Y')}"

        elif "gracias" in lower:
            return "De nada 😊"

        elif "adiós" in lower or "bye" in lower:
            return "Hasta luego 👋"

        else:
            return (
                "Recibí tu mensaje: "
                + text
            )

    def check_connection(self):

        try:
            requests.get(
                "https://www.google.com",
                timeout=5
            )

            self.api_status = "Conectado"

        except Exception:
            self.api_status = "Sin conexión"

        self.status_label.text = f"Estado: {self.api_status}"

    def show_error(self, error_text):

        popup = Popup(
            title="Error",
            content=Label(text=error_text),
            size_hint=(0.8, 0.4)
        )

        popup.open()


class VanniaAI(App):

    def build(self):

        self.title = "Vannia AI"

        return MainLayout()


if __name__ == "__main__":
    VanniaAI().run()
