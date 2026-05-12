[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv,json

version = 1.0

requirements = python3,kivy==2.3.0

orientation = portrait

fullscreen = 0

android.api = 34
android.minapi = 24
android.sdk = 34
android.ndk = 25b

android.permissions = INTERNET

presplash.color = #000000

[buildozer]

log_level = 2

warn_on_root = 1
