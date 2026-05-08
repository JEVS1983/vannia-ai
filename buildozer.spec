[app]
title = Vannia AI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy,requests,plyer,pillow

orientation = portrait

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a

android.allow_minapi_mismatch = True

[buildozer]
log_level = 2
warn_on_root = 1
