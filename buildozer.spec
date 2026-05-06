[app]

# (str) Título de la app
title = Vannia AI

# (str) Nombre del paquete
package.name = vanniaai

# (str) Dominio
package.domain = org.vannia

# (str) Carpeta del código
source.dir = .

# (list) Archivos incluidos
source.include_exts = py,png,jpg,kv

# (str) Versión
version = 1.0

# (list) Dependencias
requirements = python3,kivy

# (str) Orientación
orientation = portrait

# (bool) Pantalla completa
fullscreen = 0

# ==============================
# 🔥 ANDROID CONFIG (CLAVE)
# ==============================

# API estable (evita errores de build-tools)
android.api = 33
android.minapi = 21

# NDK correcto
android.ndk = 25b

# 🔥 SDK PATH (TU SDK de GitHub Actions)
android.sdk_path = /home/runner/work/vannia-ai/vannia-ai/android-sdk

# 🔥 FIX para compatibilidad con buildozer viejo
android.sdk = /home/runner/work/vannia-ai/vannia-ai/android-sdk

# 🔥 Arquitectura correcta (nuevo formato)
android.archs = arm64-v8a

# 🔥 Aceptar licencias automático
android.accept_sdk_license = True

# 🔥 Bootstrap estable
p4a.bootstrap = sdl2

# ==============================
# 🔐 PERMISOS
# ==============================

android.permissions = INTERNET

# ==============================
# 🛠 DEBUG (opcional)
# ==============================

android.logcat_filters = *:S python:D

# ==============================
# 🚫 EVITAR ERRORES
# ==============================

# NO usar:
# android.arch =
# android.sdk_version =
# android.api > 33
