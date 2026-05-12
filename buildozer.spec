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
source.include_exts = py,png,jpg,kv,json,txt

# (list) Files to exclude
source.exclude_exts = spec

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy==2.3.0

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# =========================
# ANDROID CONFIG
# =========================

# Android API to use
android.api = 34

# Minimum Android API
android.minapi = 24

# Android SDK version
android.sdk = 34

# Android NDK version
android.ndk = 25b

# Architecture
android.archs = arm64-v8a

# Permissions
android.permissions = INTERNET

# Android entrypoint
android.entrypoint = org.kivy.android.PythonActivity

# Use AndroidX
android.enable_androidx = True

# Accept SDK license automatically
android.accept_sdk_license = True

# Skip update checks
android.skip_update = False

# Presplash background color
presplash.color = #000000

# Window color
android.presplash_color = #000000

# App icon
#icon.filename = %(source.dir)s/icon.png

# Presplash image
#presplash.filename = %(source.dir)s/presplash.png

# Wake lock
android.wakelock = False

# Logcat filters
android.logcat_filters = *:S python:D

# Backup rules
android.allow_backup = True

# =========================
# BUILD OPTIONS
# =========================

# Copy libs instead of symlink
android.copy_libs = 1

# Use legacy storage
android.manifest.application_arguments = android:requestLegacyExternalStorage="true"

# Gradle dependencies
android.gradle_dependencies =

# Extra Java classes
android.add_jars =

# =========================
# PYTHON-FOR-ANDROID
# =========================

# Bootstrap
p4a.bootstrap = sdl2

# Python version
p4a.branch = master

# Enable debug
p4a.debug = False

# =========================
# BUILD CONFIG
# =========================

[buildozer]

# Log level
log_level = 2

# Warn on root
warn_on_root = 1
