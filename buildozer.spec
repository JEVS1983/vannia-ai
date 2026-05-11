[app]

title = Vannia AI

package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 1.0

requirements = python3,kivy==2.2.1,requests

orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25b

android.accept_sdk_license = True

android.permissions = INTERNET

android.archs = arm64-v8a

android.enable_androidx = True

android.release_artifact = apk

p4a.branch = stable

source.exclude_dirs = tests, bin, venv, .git, __pycache__

log_level = 2

window = 1

build_dir = .buildozer

osx.python_version = 3
osx.kivy_version = 2.2.1


[buildozer]

log_level = 2

warn_on_root = 1
