[app]

# (str) Título de la app
title = Vannia AI

# (str) Nombre del paquete
package.name = vanniaai

# (str) Dominio (formato inverso)
package.domain = org.vannia

# (str) Directorio del código
source.dir = .

# (list) Extensiones incluidas
source.include_exts = py,png,jpg,kv

# (str) Versión
version = 1.0

# (list) Requisitos
requirements = python3,kivy

# (str) Orientación
orientation = portrait

# 🔥 ANDROID CONFIG

# API estable (NO usar 34/37)
android.api = 33
android.minapi = 21

# NDK recomendado por python-for-android
android.ndk = 25b

# 🔥 CRÍTICO: usar TU SDK (evita errores de licencia)
android.sdk_path = /home/runner/work/vannia-ai/vannia-ai/android-sdk

# 🔥 NUEVO formato correcto
android.archs = arm64-v8a

# 🔥 Aceptar licencias automáticamente
android.accept_sdk_license = True

# 🔥 Bootstrap estable
p4a.bootstrap = sdl2

# (opcional pero recomendado)
fullscreen = 0

# (opcional)
android.permissions = INTERNET

# (opcional)
android.logcat_filters = *:S python:D

# 🔥 IMPORTANTE: evitar configs obsoletas
# NO usar:
# android.sdk =
# android.arch =
# android.api = 34+
