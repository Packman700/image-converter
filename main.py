import os

from functions.color_manipulation import *
from procedures.generate_average_rgb_list import *
from procedures.generate_file.generate_img_file import *
from procedures.generate_file.generate_HTML_file import *
from procedures.set_settings import *

### SETTINGS ###
# SETUP
settings = set_settings()

#### IMAGE TO AVERAGE RGB COLORS LIST #####
average_rgb_values_2d_list = generate_average_rgb_list(settings)

# CHANGE COLOR MODE
average_rgb_values_2d_list = change_color_mode(average_rgb_values_2d_list, settings)

# CREATE FILE

if settings.action == "pixelated_image":
    generate_img_file(average_rgb_values_2d_list, settings)
elif settings.action == "generate_HTML_file":
    generate_HTML_file(average_rgb_values_2d_list, settings)
