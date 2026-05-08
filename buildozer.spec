[app]

# (str) Title of your application
title = Vannia AI

# (str) Package name
package.name = vanniaai

# (str) Package domain
package.domain = org.vannia

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas

# (list) Files/dirs to exclude
source.exclude_dirs = tests, bin, venv, .git, __pycache__

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy,requests,plyer,pillow

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# Android API
android.api = 33

# 🔥 Compatibilidad Android vieja
android.minapi = 21

# NDK recomendada estable
android.ndk = 25b

# Arquitectura
android.archs = arm64-v8a

# Evita conflicto minsdk/ndk-api
android.allow_minapi_mismatch = True

# AndroidX
android.enable_androidx = True

# Copiar libs
android.copy_libs = 1

# Entrada Android
android.entrypoint = org.kivy.android.PythonActivity

# Tema Android
android.apptheme = "@android:style/Theme.NoTitleBar"

# Presplash opcional
# presplash.filename = %(source.dir)s/data/presplash.png

# Icono opcional
# icon.filename = %(source.dir)s/data/icon.png


[buildozer]

# Nivel de logs
log_level = 2

# Warning root
warn_on_root = 1
