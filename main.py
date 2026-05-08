import requests
import urllib3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock


# =====================================
# DESACTIVAR WARNING SSL
# =====================================
urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)

# =====================================
# URL DE TU BACKEND RENDER
# =====================================
SERVER_URL = "https://vannia-ai.onrender.com/chat"


# =====================================
# LAYOUT PRINCIPAL
# =====================================
class VanniaLayout(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(
            orientation="vertical",
            padding=15,
            spacing=15,
            **kwargs
        )

        # =========================
        # RESPUESTA IA
        # =========================
        self.output = Label(
            text="Hola, soy Vannia AI ✨",
            size_hint_y=0.8,
            halign="left",
            valign="top"
        )

        self.output.bind(
            size=self.update_text_width
        )

        # =========================
        # INPUT USUARIO
        # =========================
        self.input = TextInput(
            hint_text="Escribe un mensaje...",
            multiline=False,
            size_hint_y=0.1
        )

        # =========================
        # BOTÓN ENVIAR
        # =========================
        self.send_button = Button(
            text="Enviar",
            size_hint_y=0.1
        )

        self.send_button.bind(
            on_press=self.send_message
        )

        # =========================
        # AGREGAR WIDGETS
        # =========================
        self.add_widget(self.output)
        self.add_widget(self.input)
        self.add_widget(self.send_button)

    # =====================================
    # AJUSTAR TEXTO LABEL
    # =====================================
    def update_text_width(self, *args):

        self.output.text_size = (
            self.output.width,
            None
        )

    # =====================================
    # ENVIAR MENSAJE
    # =====================================
    def send_message(self, instance):

        mensaje = self.input.text.strip()

        if mensaje == "":
            return

        self.output.text = "Pensando..."

        Clock.schedule_once(
            lambda dt: self.ask_ai(mensaje),
            0
        )

    # =====================================
    # CONSULTAR GEMINI
    # =====================================
    def ask_ai(self, mensaje):

        try:

            response = requests.post(
                SERVER_URL,
                json={
                    "text": mensaje
                },
                verify=False,
                timeout=30
            )

            print("STATUS:", response.status_code)
            print("RESPONSE:", response.text)

            # =========================
            # VALIDAR RESPUESTA
            # =========================
            if response.status_code != 200:

                self.output.text = (
                    "Error servidor:\n"
                    + str(response.status_code)
                )

                return

            data = response.json()

            # =========================
            # RESPUESTA IA
            # =========================
            if "reply" in data:

                self.output.text = data["reply"]

            # =========================
            # ERROR BACKEND
            # =========================
            elif "error" in data:

                self.output.text = (
                    "Error:\n"
                    + data["error"]
                )

            else:

                self.output.text = str(data)

        except Exception as e:

            self.output.text = (
                "Error conexión:\n"
                + str(e)
            )


# =====================================
# APP
# =====================================
class VanniaApp(App):

    def build(self):
        return VanniaLayout()


# =====================================
# RUN
# =====================================
if __name__ == "__main__":

    VanniaApp().run()
