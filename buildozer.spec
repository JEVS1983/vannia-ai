[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.vanniaai

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt

version = 1.0

requirements = python3==3.10.11,kivy==2.2.1

orientation = portrait

fullscreen = 0

log_level = 2

warn_on_root = 1

# Android
android.api = 34
android.minapi = 24
android.sdk = 34
android.ndk = 25b

android.accept_sdk_license = True

android.permissions = INTERNET

android.archs = arm64-v8a

android.enable_androidx = True

android.allow_backup = True

# Generar APK y NO AAB
android.debug_artifact = apk

# Evitar problemas de Python 3.14
p4a.branch = stable
p4a.fork = kivy
p4a.url = https://github.com/kivy/python-for-android.git

# Compilación estable
android.skip_update = False

# Archivos incluidos
source.exclude_dirs = tests, bin, venv, .git, __pycache__

# Icono (opcional)
# icon.filename = %(source.dir)s/icon.png

# Splash (opcional)
# presplash.filename = %(source.dir)s/presplash.png

# Desktop
osx.python_version = 3
osx.kivy_version = 2.2.1

[buildozer]

log_level = 2

warn_on_root = 1
