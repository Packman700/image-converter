from procedures.generate_file.generate_img_file import *
from procedures.generate_file.generate_HTML_file import *
from functions.Settings import Settings
from MyImage import MyImage

### SETTINGS ###
# SETUP
settings = Settings()
myImage = MyImage(settings)

if settings.action == "pixelated_image":
    generate_img_file(myImage.photo_rgb_list, settings)
elif settings.action == "generate_HTML_file":
    generate_HTML_file(myImage.photo_rgb_list, settings)
