import os

from functions.color_manipulation import *
from procedures.generate_average_rgb_list import *
from procedures.generate_file.generate_img_file import *
from procedures.generate_file.generate_HTML_file import *
from procedures.set_settings import *

### SETTINGS ###
# SETUP
SETTINGS = set_settings()
image = Image.open(SETTINGS["PHOTO_NAME"])

#### IMAGE TO AVERAGE RGB COLORS LIST #####
average_rgb_values_2d_list = generate_average_rgb_list(image, SETTINGS)

# CHANGE COLOR MODE
average_rgb_values_2d_list = change_color_mode(average_rgb_values_2d_list, SETTINGS)

# CREATE FILE

if SETTINGS["ACTION"] == "pixelated_image":
    generate_img_file(average_rgb_values_2d_list, SETTINGS)
elif SETTINGS["ACTION"] == "generate_HTML_file":
    generate_HTML_file(average_rgb_values_2d_list, SETTINGS)
