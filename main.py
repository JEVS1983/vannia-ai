import requests
import urllib3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

# =========================
# DESACTIVAR WARNING SSL
# =========================
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# =========================
# URL DE TU BACKEND
# =========================
SERVER_URL = "https://TU-SERVIDOR.onrender.com/chat"

# =========================
# UI PRINCIPAL
# =========================
class VanniaLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)

        # Área de respuesta
        self.output = Label(
            text="Hola, soy Vannia AI ✨",
            size_hint_y=0.8,
            halign="left",
            valign="top"
        )

        self.output.bind(size=self.update_text_width)

        # Input
        self.input = TextInput(
            hint_text="Escribe tu mensaje...",
            multiline=False,
            size_hint_y=0.1
        )

        # Botón enviar
        self.send_button = Button(
            text="Enviar",
            size_hint_y=0.1
        )

        self.send_button.bind(on_press=self.send_message)

        # Agregar widgets
        self.add_widget(self.output)
        self.add_widget(self.input)
        self.add_widget(self.send_button)

    # =========================
    # AJUSTAR TEXTO
    # =========================
    def update_text_width(self, *args):
        self.output.text_size = (self.output.width, None)

    # =========================
    # ENVIAR MENSAJE
    # =========================
    def send_message(self, instance):

        mensaje = self.input.text.strip()

        if mensaje == "":
            return

        self.output.text = "Pensando..."

        # Ejecutar sin congelar UI
        Clock.schedule_once(lambda dt: self.ask_gemini(mensaje), 0)

    # =========================
    # CONECTAR BACKEND
    # =========================
    def ask_gemini(self, mensaje):

        try:

            response = requests.post(
                SERVER_URL,
                json={"message": mensaje},
                verify=False,
                timeout=30
            )

            data = response.json()

            if "reply" in data:
                self.output.text = data["reply"]
            else:
                self.output.text = "Error: respuesta inválida."

        except Exception as e:
            self.output.text = f"Error:\n{str(e)}"

# =========================
# APP
# =========================
class VanniaApp(App):

    def build(self):
        return VanniaLayout()

# =========================
# RUN
# =========================
if __name__ == "__main__":
    VanniaApp().run()
