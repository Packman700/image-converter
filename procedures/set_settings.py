import os
from PIL import Image
from functions.set_settings.chose_image import *

def set_settings():
    PHOTO_NAME = chose_image()
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

    return SETTINGS