[app]

title = Vannia AI

package.name = vanniaai
package.domain = org.jevs1983

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

source.include_patterns = assets/*,images/*

android.permissions = INTERNET

android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25b

android.archs = arm64-v8a

p4a.bootstrap = sdl2

p4a.branch = master

log_level = 2

warn_on_root = 0

android.accept_sdk_license = True

android.gradle_dependencies =

android.enable_androidx = True

android.allow_backup = True

android.manifest.launch_mode = singleTask

[buildozer]

log_level = 2
