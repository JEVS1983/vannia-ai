[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy==2.2.1,requests

orientation = portrait
fullscreen = 0

# Android
android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True

# Python-for-Android
p4a.branch = stable

# Permissions
android.permissions = INTERNET

# Architecture
android.archs = arm64-v8a

# Encoding
android.encoding = utf-8

# Log level
log_level = 2

# Do not copy unnecessary files
source.exclude_dirs = tests, bin, venv, .git, __pycache__

# Presplash
#presplash.filename = %(source.dir)s/data/presplash.png

# Icon
#icon.filename = %(source.dir)s/data/icon.png

# Services
#services =

# Extra args
android.enable_androidx = True

# Window
window = 1

# Build mode
build_dir = .buildozer

# Kivy options
osx.python_version = 3
osx.kivy_version = 2.2.1


[buildozer]

log_level = 2

warn_on_root = 1
