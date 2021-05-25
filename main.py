import os

from functions.color_manipulation import *
from procedures.generate_average_rgb_list import *
from procedures.generate_file.generate_img_file import *
from procedures.generate_file.generate_HTML_file import *

### SETTINGS ###
# SETUP
ROW_SIZE = 70
TEXT_STRING = "MONA-LISA-"

ACTON = "generate_HTML_file"
# ACTON = "pixelated_image"

# CHAR_MODE = "random_characters"  # mode 1
# CHAR_MODE = "next_characters"  # mode 2
CHAR_MODE = "asci_characters"  # mode 3

ASCI_SHIFT = 0  # limit to 10 and 70

# ASCI_BRIGHT_MODE = "70_grey_level"
ASCI_BRIGHT_MODE = "10_grey_level"

COLOR_MODE = "rgb"  # mode 1
# COLOR_MODE = "gray_scale"  # mode 2

# TODO color mode one color
# COLOR_MODE = "one_color"  # NOT WORKING mode only for asci_character
# COLOR = "#ffffff" # NOT WORKING

PHOTO_NAME = "MonaLisa.jpg"

image = Image.open(PHOTO_NAME)

COLUMN_SIZE = round((image.height * ROW_SIZE) / image.width)  # cross multiplication

CURRENT_PATH = os.getcwd()

SETTINGS = {"PHOTO_NAME": PHOTO_NAME,
            "ROW_SIZE": ROW_SIZE,
            "COLUMN_SIZE": COLUMN_SIZE,
            "TEXT_STRING": TEXT_STRING,
            "ACTON": ACTON,
            "CHAR_MODE": CHAR_MODE,
            "ASCI_SETTINGS": {
                "ASCI_SHIFT": ASCI_SHIFT,
                "ASCI_BRIGHT_MODE": ASCI_BRIGHT_MODE
            },
            "COLOR_MODE": COLOR_MODE,
            # "COLOR": COLOR,
            "PATH": CURRENT_PATH}

#### IMAGE TO AVERAGE RGB COLORS LIST #####
average_rgb_values_2d_list = generate_average_rgb_list(image, SETTINGS)

# CHANGE COLOR MODE
average_rgb_values_2d_list = change_color_mode(average_rgb_values_2d_list, SETTINGS)

# CREATE FILE

if ACTON == "pixelated_image":
    generate_img_file(average_rgb_values_2d_list, SETTINGS)
elif ACTON == "generate_HTML_file":
    generate_HTML_file(average_rgb_values_2d_list, SETTINGS)
