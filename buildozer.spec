[app]

# -------------------------------------------------
# APP INFO
# -------------------------------------------------

title = Vannia AI
package.name = vanniaai
package.domain = org.vannia.ai

# -------------------------------------------------
# SOURCE
# -------------------------------------------------

source.dir = .
source.main = main.py

source.include_exts = py,png,jpg,jpeg,kv,json,txt

source.include_patterns = assets/*,images/*

source.exclude_dirs = tests,venv,.git,__pycache__

source.exclude_exts = pyc,pyo,spec

# -------------------------------------------------
# VERSION
# -------------------------------------------------

version = 1.0

# -------------------------------------------------
# REQUIREMENTS
# -------------------------------------------------

requirements = python3,kivy

# -------------------------------------------------
# DISPLAY
# -------------------------------------------------

orientation = portrait

fullscreen = 0

# -------------------------------------------------
# ANDROID
# -------------------------------------------------

# Android modern compatibility
android.api = 34

# Android 7+
android.minapi = 24

# Stable NDK
android.ndk = 25b

# Only ARM64 (smaller APK + Play Store ready)
android.archs = arm64-v8a

# Permissions
android.permissions = INTERNET

# AndroidX support
android.enable_androidx = True

# Auto accept licenses
android.accept_sdk_license = True

# Bootstrap
p4a.bootstrap = sdl2

# -------------------------------------------------
# BUILD
# -------------------------------------------------

p4a.branch = master

build_dir = .buildozer

copy_libs = 1

# -------------------------------------------------
# UI
# -------------------------------------------------

presplash.color = #000000

# Cuando tengas icon.png en la raíz:
# icon.filename = icon.png

# Cuando tengas presplash.png:
# presplash.filename = presplash.png

# -------------------------------------------------
# DEBUG
# -------------------------------------------------

log_level = 2

warn_on_root = 1
