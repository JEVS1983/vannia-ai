[app]

title = Vannia AI

package.name = vanniaai
package.domain = org.jevs1983

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.permissions = INTERNET

android.api = 31
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a

p4a.bootstrap = sdl2

log_level = 2

android.accept_sdk_license = True

[buildozer]

log_level = 2
