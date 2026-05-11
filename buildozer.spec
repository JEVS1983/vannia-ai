[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.vannia.ai

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0

requirements = python3==3.10.11,kivy==2.3.0

orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a

p4a.branch = master

android.accept_sdk_license = True

log_level = 2

warn_on_root = 0

osx.python_version = 3
osx.kivy_version = 2.3.0

[buildozer]

log_level = 2

bin_dir = ./bin
