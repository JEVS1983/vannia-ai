[app]
title = Vannia AI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET

# 👇 IMPORTANTE: NO forzar AAB aquí
# android.release_artifact = aab ❌ ELIMINADO

android.logcat_filters = *:S python:D
