[app]

title = VanniaAI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv,json

version = 1.0

requirements = python3==3.10.11,kivy==2.2.1,cython==0.29.36

orientation = portrait
fullscreen = 0

android.api = 34
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a

android.permissions = INTERNET

android.accept_sdk_license = True

p4a.branch = stable

log_level = 2

warn_on_root = 1
