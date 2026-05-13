[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,ttf

version = 1.0

requirements = python3==3.10.11,kivy==2.2.1

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

# evita Python 3.14
osx.python_version = 3

log_level = 2
warn_on_root = 1


[buildozer]

log_level = 2
warn_on_root = 1
