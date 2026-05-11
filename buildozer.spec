[app]

# (str) Title of your application
title = Vannia AI

# (str) Package name
package.name = vanniaai

# (str) Package domain
package.domain = org.jevs1983

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf

# (list) Source directories and files to exclude
source.exclude_dirs = tests, bin, venv, .venv, __pycache__, .git

# (list) Source files to exclude
source.exclude_exts = spec

# (str) Version
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 1

#
# Android config
#

# Target Android API
android.api = 33

# Minimum API
android.minapi = 24

# Android SDK
android.sdk = 33

# Android NDK
android.ndk = 25b

# Android NDK API
android.ndk_api = 24

# Architectures
android.archs = arm64-v8a

# Python-for-Android branch
p4a.branch = stable

# AndroidX
android.enable_androidx = True

# Permissions
android.permissions = INTERNET

# Accept licenses automatically
android.accept_sdk_license = True

# Presplash color
android.presplash_color = #121212

# Background color
android.window_background_color = #121212

# Log level
log_level = 2

# Copy libs
android.copy_libs = 1

# Use default bootstrap
p4a.bootstrap = sdl2

# App theme
android.apptheme = "@android:style/Theme.NoTitleBar"

# Backup allowed
android.allow_backup = True

# Numeric version
android.numeric_version = 1

#
# Buildozer settings
#

[buildozer]

# Log level
log_level = 2

# Warn on root
warn_on_root = 0
