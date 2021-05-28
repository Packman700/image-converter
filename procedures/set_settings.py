import os
from PIL import Image
from functions.set_settings.chose_image import *
from functions.set_settings.set_row_size import *
from functions.set_settings.select_char_mode import *
from functions.set_settings.select_action import *
from functions.set_settings.text_string import *

def set_settings():
    # Declaration all optional arguments
    CHAR_MODE = None
    TEXT_STRING = None
    ASCI_BRIGHT_MODE = None
    ASCI_SHIFT = None

    PHOTO_NAME = chose_image()
    ROW_SIZE = set_row_size(Image.open(PHOTO_NAME).width)
    ACTION = select_action()

    if ACTION == "generate_HTML_file":
        CHAR_MODE = select_char_mode()
        TEXT_STRING = text_string(CHAR_MODE)
        if CHAR_MODE == "asci_characters":
            # ASCI_BRIGHT_MODE = "70_grey_level"
            ASCI_BRIGHT_MODE = "10_grey_level"

            ASCI_SHIFT = 0  # limit to 10 and 70


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
                "ACTION": ACTION,
                "CHAR_MODE": CHAR_MODE,
                "ASCI_SETTINGS": {
                    "ASCI_SHIFT": ASCI_SHIFT,
                    "ASCI_BRIGHT_MODE": ASCI_BRIGHT_MODE
                },
                "COLOR_MODE": COLOR_MODE,
                # "COLOR": COLOR,
                "PATH": CURRENT_PATH}

    return SETTINGS