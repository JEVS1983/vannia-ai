[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.jevs1983

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# IMPORTANTE
android.api = 34
android.minapi = 24
android.ndk = 25b

android.archs = arm64-v8a

p4a.bootstrap = sdl2

android.accept_sdk_license = True

log_level = 2

[buildozer]

log_level = 2
