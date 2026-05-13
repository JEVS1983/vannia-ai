[app]

title = Vannia AI

package.name = vanniaai
package.domain = org.vannia.ai

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt
source.exclude_dirs = tests,.git,__pycache__,venv,.venv,bin

version = 1.0

requirements = python3==3.10.11,kivy==2.2.1,requests,urllib3,idna,chardet,certifi,filetype,six

orientation = portrait

fullscreen = 0

android.api = 34
android.minapi = 24
android.ndk = 25b

p4a.bootstrap = sdl2
p4a.branch = master

android.permissions = INTERNET

android.enable_androidx = True
android.accept_sdk_license = True

android.archs = arm64-v8a

android.copy_libs = 1

android.presplash_color = #000000
android.window_background_color = #000000

android.apptheme = Theme.NoTitleBar

android.allow_backup = True

android.logcat_filters = *:S python:D

android.wakelock = False

android.private_storage = True

android.numeric_version = 1

log_level = 2

warn_on_root = 1

build_mode = debug

p4a.extra_args = --ignore-setup-py


# ---------------------------------
# ICONS / SPLASH
# ---------------------------------

# icon.filename = %(source.dir)s/data/icon.png
# presplash.filename = %(source.dir)s/data/presplash.png


# ---------------------------------
# EXTRA FILES
# ---------------------------------

android.add_jars =
android.add_activities =
android.add_src =
android.meta_data =


# ---------------------------------
# SERVICES
# ---------------------------------

services =


# ---------------------------------
# OUYA
# ---------------------------------

ouya.category = GAME
ouya.icon.filename = %(source.dir)s/data/ouya_icon.png


# ---------------------------------
# BUILD OPTIONS
# ---------------------------------

android.release_artifact = apk


[buildozer]

log_level = 2
warn_on_root = 1
