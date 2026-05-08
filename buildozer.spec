[app]
title = VanniaAI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

# 🔥 ULTRA ESTABLE (clave)
requirements = python3,kivy,requests

orientation = portrait

android.permissions = INTERNET

android.api = 33
android.minapi = 24
android.ndk_api = 21

android.archs = arm64-v8a

android.ndk = 25b

# 🧠 evita errores silenciosos en buildozer
log_level = 2
warn_on_root = 1
fullscreen = 0
