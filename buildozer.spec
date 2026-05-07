[app]

# ---------------------------------------
# APP INFO
# ---------------------------------------

title = Vannia AI
package.name = vanniaai
package.domain = org.vannia.ai

# ---------------------------------------
# SOURCE
# ---------------------------------------

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,txt
source.include_patterns = assets/*,images/*

# Main file
source.main = main.py

# ---------------------------------------
# VERSION
# ---------------------------------------

version = 1.0

# ---------------------------------------
# REQUIREMENTS
# ---------------------------------------

requirements = python3,kivy

# ---------------------------------------
# DISPLAY
# ---------------------------------------

orientation = portrait
fullscreen = 0

# ---------------------------------------
# ANDROID
# ---------------------------------------

android.api = 33
android.minapi = 21
android.ndk = 25b

# Architectures
android.archs = arm64-v8a, armeabi-v7a

# Permissions
android.permissions = INTERNET

# AndroidX
android.enable_androidx = True

# Bootstrap
p4a.bootstrap = sdl2

# ---------------------------------------
# BUILD
# ---------------------------------------

p4a.branch = master

build_dir = .buildozer

copy_libs = 1

# ---------------------------------------
# UI
# ---------------------------------------

presplash.color = #000000

# IMPORTANTE:
# Desactivado porque el archivo no existe
# Si luego agregas icon.png en la raíz,
# puedes descomentar esta línea.

# icon.filename = icon.png

# ---------------------------------------
# DEBUG
# ---------------------------------------

log_level = 2
warn_on_root = 1
