[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,requests

orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 24
android.ndk = 25b

android.archs = arm64-v8a

p4a.branch = stable

# IMPORTANTE
android.accept_sdk_license = True

# SOLO APK
build_dir = .buildozer

[buildozer]

log_level = 2
warn_on_root
