[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json

version = 1.0

requirements = python3,kivy==2.2.1

orientation = portrait

fullscreen = 0

android.api = 34
android.minapi = 24
android.sdk = 34
android.ndk = 25b
android.accept_sdk_license = True

android.permissions = INTERNET

android.archs = arm64-v8a

android.release_artifact = apk

p4a.branch = master

log_level = 2

warn_on_root = 1

# (list) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (list) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, portrait, portrait-reverse or landscape-reverse)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0


[buildozer]

log_level = 2

warn_on_root = 1
