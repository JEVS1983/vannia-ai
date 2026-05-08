[app]

title = Vannia AI

package.name = vanniaai
package.domain = org.vannia

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas

source.exclude_dirs = tests, bin, venv, .git, __pycache__

version = 1.0

requirements = python3,kivy,requests,plyer,pillow

orientation = portrait

fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a

android.allow_minapi_mismatch = True

android.enable_androidx = True

android.copy_libs = 1

android.entrypoint = org.kivy.android.PythonActivity

# 🔥 IMPORTANTE: SIN COMILLAS
android.apptheme = @android:style/Theme.NoTitleBar


[buildozer]

log_level = 2

warn_on_root = 1
