# (List the python modules that are required)
requirements = python3, kivy, opencv, google-cloud-vision, google-cloud-texttospeech, sqlite3

# Permissions for Android (access to camera, storage, etc.)
android.permissions = CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# Package name and version
package.name = medication_scanner
package.version = 1.0

# Orientation (landscape, portrait)
orientation = portrait

# (List the application source files)
source.include_exts = py,png,jpg,kv,db,mp3
