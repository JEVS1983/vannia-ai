[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json

version = 1.0

requirements = python3,kivy,requests,plyer,pillow

orientation = portrait

fullscreen = 0

android.permissions = INTERNET

android.api = 34
android.minapi = 24
android.ndk = 25b

android.archs = arm64-v8a

android.enable_androidx = True
android.accept_sdk_license = True

android.wakelock = False

log_level = 2

p4a.branch = master

window.width = 400
window.height = 700

source.exclude_dirs = tests, bin, venv, .git, __pycache__

android.copy_libs = 1

android.gradle_dependencies =

android.apptheme = "@android:style/Theme.NoTitleBar"

android.entrypoint = org.kivy.android.PythonActivity

p4a.bootstrap = sdl2


[buildozer]

log_level = 2
warn_on_root = 0
