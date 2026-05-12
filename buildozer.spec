[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.vanniaai

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,json

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

p4a.branch = stable

log_level = 2

warn_on_root = 1

osx.python_version = 3
osx.kivy_version = 2.2.1

android.gradle_dependencies =

android.enable_androidx = True

android.allow_backup = True

android.release_artifact = apk

# Evita Python 3.14
p4a.fork = kivy
p4a.url = https://github.com/kivy/python-for-android.git

# Mantener compilación estable
android.skip_update = False
