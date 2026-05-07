# ==========================================================
# 🚀 VANNIA AI - STABLE ANDROID VERSION
# ==========================================================

import os
import json
import uuid
import threading
import webbrowser

from datetime import datetime
from PIL import Image, ImageDraw

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
            json.dump(data or self.data, f, indent=2)

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

        img = Image.new("RGB", (512, 512), (30, 30, 30))

        draw = ImageDraw.Draw(img)

        draw.text(
            (40, 240),
            text[:40],
            fill=(255, 255, 255)
        )

        path = f"{BASE}/{uuid.uuid4().hex}.png"

        img.save(path)

        return path

# ==========================================================
# ENGINE
# ==========================================================

class Engine:

    def run(self, topic):

        ai = AI()

        script = ai.script(topic)

        imgs = []

        for s in script:
            imgs.append(ai.image(s))

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

        layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=10
        )

        self.input = TextInput(
            hint_text="Escribe idea",
            multiline=False,
            size_hint=(1, 0.2)
        )

        self.status = Label(
            text="Listo",
            size_hint=(1, 0.2)
        )

        btn_gen = Button(
            text="🎬 Generar"
        )

        btn_ad = Button(
            text="📺 Anuncio"
        )

        btn_premium = Button(
            text="💎 Premium"
        )

        btn_mp = Button(
            text="💳 Mercado Pago"
        )

        btn_gen.bind(on_press=self.generate)

        btn_ad.bind(on_press=self.ad)

        btn_premium.bind(on_press=self.premium)

        btn_mp.bind(
            on_press=lambda x: self.mp.buy("10")
        )

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

        self.status.text = "Listo ✔"

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
