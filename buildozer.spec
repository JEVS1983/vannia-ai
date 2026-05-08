[app]
title = VanniaAI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

# 🔥 Dependencias seguras para Android (sin crashes)
requirements = python3,kivy,requests

orientation = portrait

# 🌐 Internet necesario para Gemini
android.permissions = INTERNET

# 📱 Compatibilidad moderna (clave para tu error de instalación)
android.api = 33
android.minapi = 24

# ⚙️ Arquitecturas correctas (evita fallos de instalación)
android.archs = arm64-v8a,armeabi-v7a

# 🧠 Optimización / estabilidad
android.ndk = 25b
android.ndk_api = 21

# 🧱 Evita builds raros o incompatibles
log_level = 2
warn_on_root = 1

# 🚫 Reduce errores de empaquetado
fullscreen = 0
