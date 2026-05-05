[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

# =========================
# 🔥 DEPENDENCIAS PYTHON
# =========================
requirements = python3,kivy,pillow,gtts

# =========================
# 📱 CONFIG ANDROID
# =========================
orientation = portrait

android.api = 34
android.minapi = 21
android.ndk = 25b

# IMPORTANTE: evita conflictos con SDK nuevo
android.sdk = 34

# Arquitecturas (compatibilidad Play Store)
android.archs = arm64-v8a, armeabi-v7a

# Permisos básicos
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Generar AAB (Play Store recomendado)
android.release_artifact = aab

# =========================
# ⚙️ BUILD CONFIG
# =========================
log_level = 2
warn_on_root = 1

# Evita rebuilds innecesarios
p4a.branch = master

# =========================
# 🧠 FIX IMPORTANTE SDK
# =========================
# Evita que intente usar build-tools 37
android.enable_androidx = True
android.use_androidx = True
