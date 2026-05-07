# ==========================================================
# 🚀 VANNIA AI - NEXT GENERATION
# Android Stable + Images + History + Projects
# ==========================================================

import os
import json
import threading
import webbrowser

from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.utils import platform

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image

# ==========================================================
# OPTIONAL MOBILE FILE PICKER
# ==========================================================

try:

    from plyer import filechooser

    FILECHOOSER = True

except:

    FILECHOOSER = False

# ==========================================================
# CONFIG
# ==========================================================

BASE = "vannia_ai"

DB_FILE = f"{BASE}/db.json"

HISTORY_FILE = f"{BASE}/history.json"

os.makedirs(BASE, exist_ok=True)

FREE_DAILY = 10

BANNED = [
    "violencia",
    "arma",
    "sexo",
    "droga",
    "odio"
]

# ==========================================================
# SAFE FILTER
# ==========================================================

def safe(text):

    for w in BANNED:

        if w in text.lower():
            return "historia creativa positiva"

    return text

# ==========================================================
# DATABASE
# ==========================================================

class DB:

    def __init__(self):

        self.data = self.load()

    def load(self):

        if not os.path.exists(DB_FILE):

            data = {
                "credits": FREE_DAILY,
                "premium": False,
                "last": str(datetime.now().date())
            }

            self.save(data)

            return data

        try:

            with open(DB_FILE, "r") as f:
                return json.load(f)

        except:

            return {
                "credits": FREE_DAILY,
                "premium": False,
                "last": str(datetime.now().date())
            }

    def save(self, data=None):

        with open(DB_FILE, "w") as f:

            json.dump(
                data or self.data,
                f,
                indent=2
            )

# ==========================================================
# HISTORY SYSTEM
# ==========================================================

class History:

    def load(self):

        if not os.path.exists(HISTORY_FILE):
            return []

        try:

            with open(HISTORY_FILE, "r") as f:
                return json.load(f)

        except:

            return []

    def save(self, prompt, result):

        data = self.load()

        data.insert(0, {
            "prompt": prompt,
            "result": result,
            "date": str(datetime.now())
        })

        data = data[:20]

        with open(HISTORY_FILE, "w") as f:

            json.dump(data, f, indent=2)

# ==========================================================
# AI ENGINE
# ==========================================================

class AI:

    def script(self, topic):

        topic = safe(topic)

        return [
            f"🎥 IDEA: {topic}",
            "",
            f"Nadie esperaba esto sobre {topic}.",
            "",
            "El mundo cambia de forma inesperada.",
            "",
            "Todo terminó con un final sorprendente."
        ]

# ==========================================================
# ENGINE
# ==========================================================

class Engine:

    def run(self, topic):

        ai = AI()

        return ai.script(topic)

# ==========================================================
# MONETIZATION
# ==========================================================

class Monetization:

    def __init__(self, db):

        self.db = db

    def use(self):

        if self.db.data["premium"]:
            return True

        if self.db.data["credits"] <= 0:
            return False

        self.db.data["credits"] -= 1

        self.db.save()

        return True

    def reward(self):

        self.db.data["credits"] += 1

        self.db.save()

    def premium(self):

        self.db.data["premium"] = True

        self.db.save()

# ==========================================================
# ADS
# ==========================================================

class Ads:

    def reward(self, monet):

        monet.reward()

# ==========================================================
# BILLING
# ==========================================================

class Billing:

    def premium(self, monet):

        monet.premium()

# ==========================================================
# MERCADO PAGO
# ==========================================================

class MercadoPago:

    def buy(self, pack):

        links = {
            "10": "https://mpago.la/tu_link_10",
            "100": "https://mpago.la/tu_link_100",
            "premium": "https://mpago.la/tu_link_premium"
        }

        if pack in links:

            webbrowser.open(links[pack])

# ==========================================================
# MAIN APP
# ==========================================================

class VanniaApp(App):

    # ======================================================
    # BUILD
    # ======================================================

    def build(self):

        self.db = DB()

        self.history = History()

        self.monet = Monetization(self.db)

        self.engine = Engine()

        self.ads = Ads()

        self.billing = Billing()

        self.mp = MercadoPago()

        self.selected_image = ""

        # ==================================================
        # LAYOUT
        # ==================================================

        layout = BoxLayout(
            orientation="vertical",
            spacing=15,
            padding=15
        )

        # ==================================================
        # INPUT
        # ==================================================

        self.input = TextInput(
            hint_text="Escribe una idea...",
            multiline=False,
            size_hint=(1, 0.12),
            font_size=24
        )

        # ==================================================
        # STATUS
        # ==================================================

        self.status = Label(
            text="Vannia AI lista",
            size_hint=(1, 0.1),
            font_size=24
        )

        # ==================================================
        # IMAGE PREVIEW
        # ==================================================

        self.preview = Image(
            size_hint=(1, 0.3),
            allow_stretch=True
        )

        # ==================================================
        # RESULT AREA
        # ==================================================

        self.result = Label(
            text="Aquí aparecerá el contenido generado",
            font_size=22,
            size_hint_y=None,
            halign="left",
            valign="top"
        )

        self.result.bind(
            width=lambda s, w: setattr(
                s,
                "text_size",
                (w, None)
            )
        )

        self.result.bind(
            texture_size=lambda s, v: setattr(
                s,
                "height",
                v[1]
            )
        )

        scroll = ScrollView(
            size_hint=(1, 0.4)
        )

        scroll.add_widget(self.result)

        # ==================================================
        # BUTTONS
        # ==================================================

        btn_gen = Button(
            text="Generar",
            font_size=22
        )

        btn_img = Button(
            text="Subir Imagen",
            font_size=22
        )

        btn_history = Button(
            text="Historial",
            font_size=22
        )

        btn_ad = Button(
            text="Anuncio",
            font_size=22
        )

        btn_premium = Button(
            text="Premium",
            font_size=22
        )

        # ==================================================
        # EVENTS
        # ==================================================

        btn_gen.bind(on_press=self.generate)

        btn_img.bind(on_press=self.pick_image)

        btn_history.bind(on_press=self.show_history)

        btn_ad.bind(on_press=self.ad)

        btn_premium.bind(on_press=self.premium)

        # ==================================================
        # ADD WIDGETS
        # ==================================================

        widgets = [
            self.input,
            self.status,
            self.preview,
            scroll,
            btn_gen,
            btn_img,
            btn_history,
            btn_ad,
            btn_premium
        ]

        for w in widgets:

            layout.add_widget(w)

        return layout

    # ======================================================
    # GENERATE
    # ======================================================

    def generate(self, instance):

        if not self.monet.use():

            self.status.text = "Sin créditos"

            return

        self.status.text = "Generando..."

        threading.Thread(
            target=self.run_generation,
            daemon=True
        ).start()

    def run_generation(self):

        try:

            result = self.engine.run(
                self.input.text
            )

            text = "\n".join(result)

            self.history.save(
                self.input.text,
                text
            )

            Clock.schedule_once(
                lambda dt: self.done_success(text)
            )

        except Exception as e:

            Clock.schedule_once(
                lambda dt: self.done_error(str(e))
            )

    def done_success(self, text):

        self.result.text = text

        self.status.text = "Generación completada"

    def done_error(self, error):

        self.status.text = f"Error: {error}"

    # ======================================================
    # IMAGE PICKER
    # ======================================================

    def pick_image(self, instance):

        if not FILECHOOSER:

            self.status.text = "FileChooser no disponible"

            return

        try:

            files = filechooser.open_file()

            if files:

                self.selected_image = files[0]

                self.preview.source = self.selected_image

                self.preview.reload()

                self.status.text = "Imagen cargada"

        except Exception as e:

            self.status.text = str(e)

    # ======================================================
    # HISTORY
    # ======================================================

    def show_history(self, instance):

        data = self.history.load()

        if not data:

            self.result.text = "Sin historial"

            return

        text = ""

        for item in data[:10]:

            text += (
                f"PROMPT:\n{item['prompt']}\n\n"
            )

            text += (
                f"RESULTADO:\n{item['result']}\n\n"
            )

            text += "----------------------\n\n"

        self.result.text = text

        self.status.text = "Historial cargado"

    # ======================================================
    # ADS
    # ======================================================

    def ad(self, instance):

        self.ads.reward(self.monet)

        self.status.text = "Crédito agregado"

    # ======================================================
    # PREMIUM
    # ======================================================

    def premium(self, instance):

        self.billing.premium(self.monet)

        self.status.text = "Premium activado"

# ==========================================================
# RUN
# ==========================================================

if __name__ == "__main__":

    VanniaApp().run()
