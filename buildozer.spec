[app]

title = Vannia AI

package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3==3.10.11,kivy==2.2.1,requests

orientation = portrait

fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 24
android.ndk = 25b

p4a.branch = master

log_level = 2

warn_on_root = 1

[buildozer]

log_level = 2
warn_on_root = 1
