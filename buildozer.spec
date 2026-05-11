[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3==3.10.11,kivy==2.3.0,requests

orientation = portrait

fullscreen = 0

android.permissions = INTERNET

android.api = 34
android.minapi = 24
android.ndk = 25b

android.accept_sdk_license = True

presplash.color = #000000

icon.filename = icon.png

log_level = 2

warn_on_root = 1


[buildozer]

log_level = 2

warn_on_root = 1
