[app]

title = Vannia AI

package.name = vanniaai

package.domain = org.vannia

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,json

version = 1.0

requirements = python3,kivy,requests,plyer,pillow

orientation = portrait

fullscreen = 0

# Icono opcional
# icon.filename = icon.png

# Splash opcional
# presplash.filename = presplash.png

# Permisos Android
android.permissions = INTERNET

# Android moderno
android.api = 34
android.minapi = 24
android.ndk = 25b

# Arquitectura
android.archs = arm64-v8a

# AndroidX
android.enable_androidx = True

# Evita conflictos
android.accept_sdk_license = True

# Mantener pantalla activa
android.wakelock = False

# Logs
log_level = 2

# Build limpio
p4a.branch = master

# Compilar en modo debug
# android.release_artifact = apk

# Tamaño ventana desktop
window.width = 400
window.height = 700

# Evitar empaquetar basura
source.exclude_dirs = tests, bin, venv, .git, __pycache__

# Copiar librerías
android.copy_libs = 1

# Mejor compatibilidad
android.gradle_dependencies =

# Tema
android.apptheme = "@android:style/Theme.NoTitleBar"

# Entrada Android
android.entrypoint = org.kivy.android.PythonActivity

# Orientación
orientation = portrait

# No usar setup.py
p4a.bootstrap = sdl2


[buildozer]

log_level = 2

warn_on_root = 0
