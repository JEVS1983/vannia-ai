[app]

# (str) Title of your application
title = Vannia AI

# (str) Package name
package.name = vanniaai

# (str) Package domain
package.domain = org.vannia.ai

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,json,txt

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# Android API
android.api = 33

# Minimum API
android.minapi = 21

# Android NDK version
android.ndk = 25b

# Permissions
android.permissions = INTERNET

# Presplash background color
presplash.color = #000000

# App icon
icon.filename = icon.png

# (int) Log level
log_level = 2

# (int) Warn on root
warn_on_root = 1

# Build mode
p4a.branch = master

# Android architecture
android.archs = arm64-v8a, armeabi-v7a

# Enable AndroidX
android.enable_androidx = True

# Kivy version bootstrap
p4a.bootstrap = sdl2

# Recommended Gradle options
android.gradle_dependencies =

# Disable byte compile
android.copy_libs = 1

# Debug
build_dir = .buildozer

# Entry point
source.main = main.py
