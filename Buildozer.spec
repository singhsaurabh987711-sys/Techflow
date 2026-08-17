[app]

title = Techflow
package.name = techflow
package.domain = org.techflow

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json
source.main = main.py

version = 1.0

requirements = python3==3.11.9,kivy==2.3.0

orientation = portrait
fullscreen = 0

android.accept_sdk_license = True
android.api = 35
android.minapi = 21

[buildozer]

log_level = 2
warn_on_root = 1
