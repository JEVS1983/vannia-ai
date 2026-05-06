[app]

# (str) Title of your application
title = Vannia AI

# (str) Package name
package.name = vanniaai

# (str) Package domain (required)
package.domain = org.vannia

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,json

# (list) Excluded files
source.exclude_exts = spec

# (str) Application version
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy

# 🔥 Si usas más librerías, agrégalas aquí:
# requirements = python3,kivy,requests,urllib3,certifi

# (str) Orientation
orientation = portrait

# (str) Fullscreen
fullscreen = 0

# (str) Icon
icon.filename = %(source.dir)s/icon.png

# (str) Presplash
presplash.filename = %(source.dir)s/presplash.png


# ==========================================================
# ANDROID CONFIG
# ==========================================================

[buildozer]

log_level = 2
warn_on_root = 1


[app:android]

# ✅ API estable recomendada
android.api = 33

# ✅ mínimo soportado Play Store
android.minapi = 21

# ✅ NDK compatible con p4a
android.ndk = 25b

# ✅ Arquitecturas modernas
android.archs = arm64-v8a, armeabi-v7a

# ✅ Permisos básicos (ajusta según tu app)
android.permissions = INTERNET

# (str) Entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Theme
android.apptheme = "@android:style/Theme.NoTitleBar"

# (bool) Skip update
android.skip_update = False


# ==========================================================
# BUILD OPTIONS
# ==========================================================

# (bool) Use AAB (Play Store recomendado)
android.release_artifact = aab

# (bool) Debug symbols
android.debug_symbols = False

# (str) Logcat filters
android.logcat_filters = *:S python:D


# ==========================================================
# KEYSTORE (para release real)
# ==========================================================

# ⚠️ SOLO cuando firmes APK/AAB para Play Store
# android.keystore = my-release-key.keystore
# android.keystore_passwd = password
# android.keyalias = my-key-alias
# android.keyalias_passwd = password
