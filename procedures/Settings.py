import os
from PIL import Image
from .TextModeSelectMenu import TextModeSelectMenu
from options import OPTIONS

class Settings:
    # DECLARATION OF ALL OPTIONS
    source_path = image = width_size = action = char_mode = text_string = asci_bright_mode = asci_shift \
         = color_mode = eight_bit_color_mode = column_size = output_path = None

    def gui_mode_set_settings(self, gui_settings):
        self.source_path = gui_settings["source_path"]
        self.width_size = gui_settings["row_size"]
        self.action = gui_settings["action"]
        self.char_mode = gui_settings["char_mode"]
        self.text_string = gui_settings["text_string"]
        self.asci_bright_mode = gui_settings["asci_bright_mode"]
        self.asci_shift = gui_settings["asci_shift"]
        self.color_mode = gui_settings["color_mode"]
        self.eight_bit_color_mode = gui_settings["eight_bit_color_mode"]
        self.output_path = gui_settings["output_path"]
        self.image = Image.open(gui_settings["source_path"])
        self.column_size = (self.image.height * self.width_size) // self.image.width

    def text_mode_set_settings(self):
        select_menu = TextModeSelectMenu()

        self.choose_photo_path()
        self.create_image()
        self.set_row_size()
        self.action = select_menu.create_menu("Select Action", OPTIONS["ACTION"])
        self.choose_output_path()
        if self.action == "generate_HTML_file":
            self.char_mode = select_menu.create_menu("Select Char Mode", OPTIONS["CHAR_MODE"])
            if self.char_mode in ["random_characters", "next_characters"]:
                self.text_string = input("Write string with you want to use in picture: ")

            if self.char_mode == "asci_characters":
                self.asci_bright_mode = select_menu.create_menu("Select ASCI Mode", OPTIONS["ASCI_BRIGHT"])
                self.set_asci_shift()

        self.color_mode = select_menu.create_menu("Select Color Mode", OPTIONS["COLOR_MODE"])
        if self.color_mode == "8_bit":
            self.eight_bit_color_mode = select_menu.create_menu("Select 8 Bit Color Mode", OPTIONS["8\_BIT_COLOR"])

        # IF PROGRAM WILL RETURN STRANGE THINGS RETURN TO THIS VERSION
        # self.column_size = round((self.image.height * self.row_size) / self.image.width)
        self.column_size = (self.image.height * self.row_size) // self.image.width

    def choose_photo_path(self):
        while True:
            source_path = input("Write path to photo: ")
            try:
                img = Image.open(source_path)
                img.verify()  # I perform also verify, don't know if he sees other types o defects
                img.close()
            except FileNotFoundError:
                print("File not found")
                continue
            except Image.UnidentifiedImageError:
                print("Selected file isn't image")
                continue
            except IsADirectory:
                print("Please give also file name")
                continue

            self.source_path = source_path
            break

    def choose_output_path(self):
        LEGAL_PHOTO_EXTENSION = [".png", ".bmp", ".gif", ".jpg", ".jpeg", ".tff", ".tiff", ".eps"]
        while True:

            path = input("Write output name file or path: ")
            _ , extension = os.path.splitext(path)
            dir_name = os.path.dirname(path)

            if self.action == "generate_HTML_file":
                if extension != ".html":
                    print("Your file must have .html file extension ")
                    continue
            elif self.action == "pixelated_image":
                if extension not in LEGAL_PHOTO_EXTENSION:
                    print("Your file must use photo file extension (like .png or .jpg)")
                    continue

            if not dir_name:
                self.output_path = path
                break

            if not os.path.dirname(dir_name):
                print("Wrong path")
                continue

            self.output_path = path
            break

    def create_image(self):
        self.image = Image.open(self.source_path)

    def set_row_size(self):
        while True:
            try:
                row_size = float(input(f"Chose row size (value between 1 to {self.image.width}): "))
            except (TypeError, ValueError):
                print("You must write number")
                continue

            if row_size > self.image.width:
                print("Row size cant be bigger than photo")
                continue
            elif row_size < 1:
                print("Row size cant be smaller than 1")
                continue
            elif row_size % 1 != 0:
                print("Row size must be integer")
                continue

            self.width_size = int(row_size)
            break

    def set_asci_shift(self):
        while True:
            asci_shift = 0

            try:
                if self.asci_bright_mode in ["10_grey_level", "reverse_10_grey_level"]:
                    asci_shift = float(input("Set shift between -0 to 10: "))
                    if not 0 <= asci_shift <= 10:
                        print("Shift must be between 0 and 10 try again")
                        continue
                elif self.asci_bright_mode in ["70_grey_level", "reverse_70_grey_level"]:
                    asci_shift = float(input("Set shift between 0 to 70: "))
                    if not 0 <= asci_shift <= 70:
                        print("Shift must be between 0 and 70 try again")
                        continue
            except (TypeError, ValueError):
                print("You must write number")

            if asci_shift % 1 != 0:
                print("asci_shift must be integer")
                continue

            self.asci_shift = int(asci_shift)
            break
