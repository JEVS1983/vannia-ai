```ini
[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

version = 0.1

requirements = python3==3.10.11,kivy==2.3.0

orientation = portrait

fullscreen = 0

# Entry point
source.main = main.py


# =========================
# Android configuration
# =========================

android.api = 34
android.minapi = 24
android.sdk = 34

# Stable NDK
android.ndk = 25b

# Architecture
android.archs = arm64-v8a

# Bootstrap
p4a.bootstrap = sdl2

# Permissions
android.permissions = INTERNET

# AndroidX
android.enable_androidx = True

# Faster startup
android.accept_sdk_license = True

# App behavior
android.wakelock = False

# Splash screen
presplash.color = #121212

# Icon
#icon.filename = %(source.dir)s/data/icon.png

# Presplash image
#presplash.filename = %(source.dir)s/data/presplash.png

# Window color
android.statusbar_color = #121212
android.navigationbar_color = #121212

# Prevent Python 3.14 issues
p4a.branch = stable

# Log level
log_level = 2

# Copy libs
android.copy_libs = 1

# Build mode
android.release_artifact = apk

# Use SDL2
osx.kivy_version = 2.3.0

# Exclude unnecessary files
source.exclude_dirs = tests, bin, venv, .git, __pycache__

source.exclude_patterns = *.pyc,*.pyo,*.git*

# =========================
# Buildozer
# =========================

[buildozer]

warn_on_root = 1

# Recommended for GitHub Actions
build_dir = .buildozer
bin_dir = ./bin
```
