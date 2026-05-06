[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv,mp3

version = 1.0

requirements = python3,kivy,pillow,gtts

orientation = portrait
fullscreen = 0

log_level = 2

android.permissions = INTERNET

# 🔥 CONFIG ANDROID ESTABLE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# 🔥 NUEVO FORMATO (IMPORTANTE)
android.archs = arm64-v8a

# 🔥 EVITA ERRORES
android.accept_sdk_license = True
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1
