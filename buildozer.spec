[app]
title = VanniaAI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

# 🔥 Dependencias seguras (evita crashes Android)
requirements = python3,kivy,requests

orientation = portrait

# 🌐 Permiso esencial para Gemini API
android.permissions = INTERNET

# 📱 Compatibilidad REAL con Android actual
android.api = 33
android.minapi = 24
android.ndk_api = 21

# ⚙️ Arquitectura estable (evita errores de instalación)
android.archs = arm64-v8a

# 🧠 Estabilidad de compilación
android.ndk = 25b
log_level = 2
warn_on_root = 1

# 🚫 Evita problemas visuales raros
fullscreen = 0
