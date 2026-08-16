[app]

# (str) Title of your application
title = Techflow
version = 1.0
android.accept_sdk_license = True
# (str) Package name
package.name = techflow

# (str) Package domain
package.domain = org.techflow

# (str) Source code directory
source.dir = .

# (str) Main Python file
source.main = main.py

# (list) Application requirements
requirements = python3,kivy==2.3.0

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0


[buildozer]

# (str) Log level
log_level = 2

# (str) Warning when running as root
warn_on_root = 1
