[app]
title = VanniaAI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy,requests

orientation = portrait

android.permissions = INTERNET

# 🔥 Compatibilidad real Android moderno
android.api = 33
android.minapi = 24
android.ndk_api = 21

# ⚙️ arquitectura segura
android.archs = arm64-v8a

android.ndk = 25b

# 🔥 clave para evitar tu error de mismatch
android.allow_minsdk_ndkapi_mismatch = True

log_level = 2
warn_on_root = 1
fullscreen = 0
