[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy,pillow,gtts

orientation = portrait

android.permissions = INTERNET

android.archs = arm64-v8a, armeabi-v7a

android.release_artifact = aab

[buildozer]

log_level = 2
warn_on_root = 1
