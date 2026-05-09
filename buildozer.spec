[app]

title = Vannia AI

package.name = vanniaai

package.domain = org.vannia

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt

version = 1.0

requirements = python3,kivy==2.3.0,requests,urllib3,certifi,idna,chardet

orientation = portrait

fullscreen = 0

source.include_patterns = assets/*,images/*

presplash.filename =

icon.filename =

android.permissions = INTERNET

android.api = 34

android.minapi = 24

android.ndk = 25b

android.archs = arm64-v8a

android.accept_sdk_license = True

p4a.bootstrap = sdl2

log_level = 2

warn_on_root = 1


[buildozer]

log_level = 2

warn_on_root = 1
