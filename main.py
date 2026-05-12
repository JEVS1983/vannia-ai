from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (0.1, 0.1, 0.1, 1)


class ChatApp(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=10, **kwargs)

        self.chat = Label(
            text="🤖 Vannia AI lista",
            size_hint=(1, 0.8)
        )

        self.input = TextInput(
            hint_text="Escribe aquí",
            multiline=False,
            size_hint=(1, 0.1)
        )

        self.button = Button(
            text="Enviar",
            size_hint=(1, 0.1)
        )

        self.button.bind(on_press=self.send_message)

        self.add_widget(self.chat)
        self.add_widget(self.input)
        self.add_widget(self.button)

    def send_message(self, instance):

        text = self.input.text.strip()

        if text == "":
            return

        self.chat.text = f"🧑 {text}\n🤖 Recibido correctamente"

        self.input.text = ""


class VanniaAI(App):

    def build(self):
        return ChatApp()


if __name__ == "__main__":
    VanniaAI().run()
