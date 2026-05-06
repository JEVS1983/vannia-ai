[app]

title = Vannia AI
package.name = vanniaai
package.domain = org.vannia

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

# =========================
# 🧠 PYTHON DEPENDENCIAS
# =========================
requirements = python3,kivy,pillow,gtts

# =========================
# 📱 ANDROID CONFIG ESTABLE
# =========================
orientation = portrait

android.api = 34
android.minapi = 21
android.ndk = 25b

# 🔥 CLAVE: evitar SDK automático problemático
android.sdk = 34

# Arquitecturas Play Store
android.archs = arm64-v8a, armeabi-v7a

# Permisos básicos
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Generar AAB (Play Store)
android.release_artifact = aab

# =========================
# ⚙️ FIX IMPORTANTE CI/CD
# =========================
# Evita conflictos con versiones nuevas de SDK
android.enable_androidx = True
android.use_androidx = True

# 🔥 IMPORTANTE: fuerza comportamiento estable
p4a.branch = master

# Logs más claros
log_level = 2
warn_on_root = 1
