[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json

version = 1.0

requirements = python3,kivy==2.2.1,requests,urllib3,idna,chardet,certifi,filetype,six

orientation = portrait

fullscreen = 0

# Android
android.api = 34
android.minapi = 24
android.ndk = 25b

android.accept_sdk_license = True

android.permissions = INTERNET

android.archs = arm64-v8a

# IMPORTANTE
android.release_artifact = apk

p4a.bootstrap = sdl2
p4a.branch = stable

source.exclude_dirs = venv,.venv,bin,.git,__pycache__,build,.buildozer

log_level = 2

warn_on_root = 1

[buildozer]

log_level = 2
bin_dir = ./bin
