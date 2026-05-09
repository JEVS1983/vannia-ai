import requests
from threading import Thread

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.window import Window

from plyer import tts


# COLOR APP
Window.clearcolor = (0.08, 0.08, 0.10, 1)


# URL RENDER
SERVER_URL = "https://vannia-ai.onrender.com/chat"


class ChatBubble(Label):
    def __init__(self, text, user=False, **kwargs):
        super().__init__(**kwargs)

        self.text = text
        self.size_hint_y = None
        self.text_size = (Window.width * 0.8, None)
        self.halign = "left"
        self.valign = "middle"
        self.padding = [20, 20]
        self.markup = True

        self.bind(texture_size=self.update_height)

        if user:
            self.color = (1, 1, 1, 1)
        else:
            self.color = (0.7, 1, 0.8, 1)

    def update_height(self, *args):
        self.height = self.texture_size[1] + 40


class VanniaLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=10, padding=10, **kwargs)

        title = Label(
            text="[b]Vannia AI[/b]",
            markup=True,
            size_hint_y=None,
            height=60,
            font_size=28,
            color=(1, 1, 1, 1)
        )

        self.add_widget(title)

        self.scroll = ScrollView()

        self.chat_layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            size_hint_y=None
        )

        self.chat_layout.bind(
            minimum_height=self.chat_layout.setter("height")
        )

        self.scroll.add_widget(self.chat_layout)

        self.add_widget(self.scroll)

        bottom = BoxLayout(size_hint_y=None, height=60, spacing=10)

        self.input_text = TextInput(
            hint_text="Escribe un mensaje...",
            multiline=False,
            background_color=(0.15, 0.15, 0.18, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1)
        )

        send_button = Button(
            text="Enviar",
            size_hint_x=None,
            width=120,
            background_color=(0.2, 0.6, 1, 1)
        )

        send_button.bind(on_press=self.send_message)

        bottom.add_widget(self.input_text)
        bottom.add_widget(send_button)

        self.add_widget(bottom)

        self.add_message(
            "Hola, soy Vannia AI ✨ ¿En qué puedo ayudarte hoy?",
            user=False
        )

    def add_message(self, text, user=False):
        bubble = ChatBubble(text=text, user=user)
        self.chat_layout.add_widget(bubble)

        Clock.schedule_once(lambda dt: setattr(self.scroll, 'scroll_y', 0))

    def send_message(self, instance):
        text = self.input_text.text.strip()

        if not text:
            return

        self.add_message(f"Tú: {text}", user=True)

        self.input_text.text = ""

        Thread(target=self.get_ai_response, args=(text,), daemon=True).start()

    def get_ai_response(self, text):
        try:
            response = requests.post(
                SERVER_URL,
                json={"text": text},
                timeout=60
            )

    VanniaApp().run()
