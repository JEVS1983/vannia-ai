[app]

# (str) Title of your application
title = Vannia AI

# (str) Package name
package.name = vanniaai

# (str) Package domain
package.domain = org.vannia.ai

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt,json

# (list) Files to exclude
source.exclude_dirs = tests,.git,__pycache__,venv,.venv,bin

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3==3.10.11,kivy==2.2.1,requests,urllib3,idna,chardet,certifi,filetype,six

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# (int) Android API to use
android.api = 34

# (int) Minimum API required
android.minapi = 24

# (str) Android NDK version
android.ndk = 25b

# (str) Android SDK version
android.sdk = 34

# (str) Bootstrap
p4a.bootstrap = sdl2

# (str) Python-for-Android branch
p4a.branch = master

# (list) Android permissions
android.permissions = INTERNET

# (bool) Use AndroidX
android.enable_androidx = True

# (bool) Copy libs
android.copy_libs = 1

# (str) Architecture
android.archs = arm64-v8a

# (int) Log level
log_level = 2

# (bool) Warn on root
warn_on_root = 1

# (str) Presplash color
android.presplash_color = #000000

# (str) Window background color
android.window_background_color = #000000

# (bool) Enable backup
android.allow_backup = True

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# (str) Entry point
entrypoint = main.py

# (str) Theme
android.apptheme = Theme.NoTitleBar

# (str) Release artifact
# android.release_artifact = apk

# (str) Private storage
android.private_storage = True

# (bool) Skip update
android.skip_update = False

# (str) Gradle dependencies
android.gradle_dependencies =

# (str) Extra manifest XML
android.extra_manifest_xml =

# (str) Extra manifest application arguments
android.extra_manifest_application_arguments =

# (str) Services
services =

# (str) OUYA category
ouya.category = GAME

# (str) OUYA icon filename
ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (bool) Indicate if the application should stay on
android.wakelock = False

# (list) Android add jars
android.add_jars =

# (list) Android add activities
android.add_activities =

# (str) Whitelist
android.whitelist =

# (str) Blacklist
android.blacklist_src =

# (str) Add source
android.add_src =

# (str) Meta-data
android.meta_data =

# (str) Presplash filename
presplash.filename =

# (str) Icon filename
icon.filename =

# (str) Adaptive icon foreground
icon.adaptive_foreground.filename =

# (str) Adaptive icon background
icon.adaptive_background.filename =

# (bool) Enable adb arguments
android.adb_args =

# (str) Gradle repositories
android.gradle_repositories =

# (str) Numeric version
android.numeric_version = 1

# (bool) Enable logs
android.logcat_filters = *:S python:D

# (str) Home app
android.home_app = False

# (str) Extra args
p4a.extra_args = --ignore-setup-py

# (str) Build mode
build_mode = debug


[buildozer]

# (int) Log level
log_level = 2

# (int) Display warning if run as root
warn_on_root = 1
