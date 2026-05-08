[app]

# =========================
# APP INFO
# =========================
title = Vannia AI
package.name = vanniaai
package.domain = org.vannia

# =========================
# SOURCE
# =========================
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt

# Excluir carpetas innecesarias
source.exclude_dirs = tests, bin, venv, .git, __pycache__

# =========================
# VERSION
# =========================
version = 1.0

# =========================
# REQUIREMENTS
# =========================
requirements = python3,kivy,requests,plyer,pillow

# =========================
# SCREEN
# =========================
orientation = portrait
fullscreen = 0

# =========================
# ANDROID
# =========================

# Permisos
android.permissions = INTERNET

# 🔥 Android moderno
android.api = 34

# 🔥 Compatibilidad Android viejo
android.minapi = 21

# NDK estable
android.ndk = 25b

# Arquitectura
android.archs = arm64-v8a

# Evita conflicto minsdk/ndkapi
android.allow_minapi_mismatch = True

# AndroidX
android.enable_androidx = True

# Copiar librerías
android.copy_libs = 1

# Entry point Android
android.entrypoint = org.kivy.android.PythonActivity

# Tema Android
android.apptheme = @android:style/Theme.NoTitleBar

# =========================
# OPTIONAL ICONS
# =========================

# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

# =========================
# BUILD
# =========================
[buildozer]

log_level = 2
warn_on_root = 1
