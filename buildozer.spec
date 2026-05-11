[app]

# (str) Title of your application
title = Vannia AI

# (str) Package name
package.name = vanniaai

# (str) Package domain
package.domain = org.jevs1983

# (str) Source code directory
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf

# (list) Source directories to exclude
source.exclude_dirs = tests,bin,venv,.venv,__pycache__,.git

# (list) Source files to exclude
source.exclude_exts = spec

# (str) Version
version = 0.1

# (list) Requirements
requirements = python3,kivy

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 1

#
# Android Configuration
#

# Android API target
android.api = 33

# Minimum Android API
android.minapi = 24

# Android NDK version
android.ndk = 28c

# Android architectures
android.archs = arm64-v8a

# Python-for-Android branch
p4a.branch = master

# Bootstrap
p4a.bootstrap = sdl2

# Enable AndroidX
android.enable_androidx = True

# Permissions
android.permissions = INTERNET

# Accept SDK licenses automatically
android.accept_sdk_license = True

# Copy shared libraries
android.copy_libs = 1

# App theme
android.apptheme = "@android:style/Theme.NoTitleBar"

# Presplash color
android.presplash_color = #121212

# Window background color
android.window_background_color = #121212

# Backup support
android.allow_backup = True

# Numeric version
android.numeric_version = 1

# Logging level
log_level = 2

#
# Buildozer settings
#

[buildozer]

# Log level
log_level = 2

# Warn if
