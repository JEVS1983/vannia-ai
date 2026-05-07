# ==========================================================
# 🚀 VANNIA AI - ANDROID STABLE UI
# ==========================================================

import os
import json
import threading
import webbrowser

from datetime import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.utils import platform

# ==========================================================
# CONFIG
# ==========================================================

BASE = "vannia_ai"
DB_FILE = f"{BASE}/db.json"

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
# AI ENGINE
# ==========================================================

class AI:

    def script(self, topic):

        topic = safe(topic)

        return [
            f"Nadie esperaba esto sobre {topic}",
            "El mundo cambia de forma inesperada",
            "Final sorprendente"
        ]

    def image(self, text):

        # Simulación estable Android
        return "ok"

# ==========================================================
# ENGINE
# ==========================================================

class Engine:

    def run(self, topic):

        ai = AI()

        script = ai.script(topic)

        # Simulación temporal estable
        imgs = script

        return imgs

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

        if platform != "android":

            monet.reward()

            return

        print("Rewarded Ad placeholder")

# ==========================================================
# BILLING
# ==========================================================

class Billing:

    def premium(self, monet):

        if platform != "android":

            monet.premium()

            return

        print("Premium placeholder")

    def credits(self, monet, amount):

        if platform != "android":

            monet.db.data["credits"] += amount

            monet.db.save()

            return

        print("Credits placeholder")

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

    def build(self):

        self.db = DB()

        self.monet = Monetization(self.db)

        self.engine = Engine()

        self.ads = Ads()

        self.billing = Billing()

        self.mp = MercadoPago()

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
            hint_text="Escribe una idea",
            multiline=False,
            size_hint=(1, 0.15),
            font_size=24
        )

        # ==================================================
        # STATUS
        # ==================================================

        self.status = Label(
            text="Listo",
            size_hint=(1, 0.12),
            font_size=28
        )

        # ==================================================
        # BUTTONS
        # ==================================================

        btn_gen = Button(
            text="Generar",
            font_size=24
        )

        btn_ad = Button(
            text="Anuncio",
            font_size=24
        )

        btn_premium = Button(
            text="Premium",
            font_size=24
        )

        btn_mp = Button(
            text="Mercado Pago",
            font_size=24
        )

        # ==================================================
        # EVENTS
        # ==================================================

        btn_gen.bind(on_press=self.generate)

        btn_ad.bind(on_press=self.ad)

        btn_premium.bind(on_press=self.premium)

        btn_mp.bind(
            on_press=lambda x: self.mp.buy("10")
        )

        # ==================================================
        # ADD WIDGETS
        # ==================================================

        widgets = [
            self.input,
            self.status,
            btn_gen,
            btn_ad,
            btn_premium,
            btn_mp
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

            self.engine.run(self.input.text)

            Clock.schedule_once(
                lambda dt: self.done_success()
            )

        except Exception as e:

            Clock.schedule_once(
                lambda dt: self.done_error(str(e))
            )

    def done_success(self):

        self.status.text = "Listo"

    def done_error(self, error):

        self.status.text = f"Error: {error}"

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
