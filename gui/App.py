from tkinter import *
from tkinter.filedialog import (asksaveasfilename)
from .MyLabelFrame import MyLabelFrame
from .ChoosePhotoButton import ChoosePhotoButton
from .GenerateFileButton import GenerateFileButton
from .CustomSpinBox import CustomSpinBox
from .RadioButtons import RadioButtons
from options import OPTIONS
from .SetTextString import SetTextString
from PIL import Image

from procedures.Settings import Settings
from MyImage import MyImage
from procedures.PresentData import PresentData

class App(Frame):
    def __init__(self):
        super().__init__()
        self.pack()

        # Set variables
        self.is_photo_chosen = BooleanVar(None, False)
        self.is_html_mode = BooleanVar(None, False)
        self.is_need_text_string = BooleanVar(None, False)  # True if char_mode is random or next strings
        self.is_asci_char_mode = BooleanVar(None, False)
        self.is_8_bit_mode = BooleanVar(None, False)
        self.width_size = IntVar(None)
        self.max_asci_shift = IntVar(None)

        # Create widgets
        ### GENERAL SETTINGS ###
        self.choose_photo_button = ChoosePhotoButton(self)

        general_settings_frame = MyLabelFrame(self, "General Settings")
        self.set_row_size_spinbox = CustomSpinBox(general_settings_frame.get(), self.width_size, 1, "Chose output width: ", self.is_photo_chosen)
        self.select_action_radio = RadioButtons(general_settings_frame.get(), OPTIONS["ACTION"], "Select action", self.is_photo_chosen)
        ### HTML SETTINGS ###
        html_settings_frame = MyLabelFrame(self, "Html Settings")
        self.select_char_mode = RadioButtons(html_settings_frame.get(), OPTIONS["CHAR_MODE"], "Select char mode", self.is_html_mode)
        self.set_text_string = SetTextString(html_settings_frame.get(), "Entry text: ", self.is_need_text_string)
        self.select_asci_mode = RadioButtons(html_settings_frame.get(), OPTIONS["ASCI_BRIGHT"], "Select asci mode", self.is_asci_char_mode)
        self.set_asci_shift_spinbox = CustomSpinBox(html_settings_frame.get(), self.max_asci_shift, 0, "Set asci shift", self.is_asci_char_mode)

        ### COLOR SETTINGS ###
        color_settings_frame = MyLabelFrame(self, "Html Color")
        self.select_color_mode = RadioButtons(color_settings_frame.get(), OPTIONS["COLOR_MODE"], "Select color mode", self.is_photo_chosen)
        self.select_8_bit_mode = RadioButtons(color_settings_frame.get(), OPTIONS["8_BIT_COLOR"], "Select 8 bit mode", self.is_8_bit_mode)

        self.generate_picture_button = GenerateFileButton(self, self.main_logic, "Generate picture", self.is_photo_chosen)

        # Create widget variables listeners
        self.choose_photo_button.get().trace("wr", self.photo_path_trace)
        self.select_action_radio.get().trace("wr", self.select_action_radio_trace)
        self.select_char_mode.get().trace("wr", self.select_char_mode_trace)
        self.select_color_mode.get().trace("wr", self.select_color_mode_trace)
        self.select_asci_mode.get().trace("wr", self.select_asci_mode_trace)

        # Print widgets
        self.choose_photo_button.grid(row=1, column=0, sticky="ew")

        general_settings_frame.grid(row=2, column=0, sticky="ns")
        self.select_action_radio.pack()
        self.set_row_size_spinbox.pack()

        html_settings_frame.grid(row=3, column=0, columnspan=2, sticky="ew")
        self.select_char_mode.grid(row=0, column=0)
        self.set_text_string.grid(row=1, column=0)
        self.select_asci_mode.grid(row=0, column=1)
        self.set_asci_shift_spinbox.grid(row=1, column=1)

        color_settings_frame.grid(row=1, rowspan=2, column=1, sticky="ns")
        self.select_color_mode.pack()
        self.select_8_bit_mode.pack()

        self.generate_picture_button.grid(row=4, column=1, sticky="e")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
    # Listeners
    def photo_path_trace(self, *args):
        if self.choose_photo_button.get_value():
            self.is_photo_chosen.set(True)
            photo_width = Image.open(self.choose_photo_button.get_value()).width
            self.width_size.set(photo_width)
        else:
            self.is_photo_chosen.set(False)

    def select_action_radio_trace(self, *args):
        if self.select_action_radio.get_value() == "generate_HTML_file" and self.is_photo_chosen.get():
            self.is_html_mode.set(True)
        else:
            self.is_html_mode.set(False)

    def select_char_mode_trace(self, *args):
        if not self.is_html_mode.get():
            self.is_need_text_string.set(False)
            self.is_asci_char_mode.set(False)
        elif self.select_char_mode.get_value() in ["next_characters", "random_characters"]:
            self.is_need_text_string.set(True)
            self.is_asci_char_mode.set(False)
        else:
            self.is_need_text_string.set(False)
            self.is_asci_char_mode.set(True)

    def select_color_mode_trace(self, *args):
        if not self.is_photo_chosen.get():
            self.is_8_bit_mode.set(False)
        if self.select_color_mode.get_value() == "8_bit":
            self.is_8_bit_mode.set(True)
        else:
            self.is_8_bit_mode.set(False)

    def select_asci_mode_trace(self, *args):
        if self.select_asci_mode.get_value() in ["10_grey_level", "reverse_10_grey_level"]:
            self.max_asci_shift.set(10)
        elif self.select_asci_mode.get_value() in ["70_grey_level", "reverse_70_grey_level"]:
            self.max_asci_shift.set(70)

    # Other
    def main_logic(self):
        gui_settings = {
            "source_path": self.choose_photo_button.get_value(),
            "row_size": int(self.set_row_size_spinbox.get_value()),
            "action": self.select_action_radio.get_value(),
            "char_mode": None, "text_string": None,
            "asci_bright_mode": None, "asci_shift": None,
            "color_mode": None, "eight_bit_color_mode": None,
            "output_path": None,
        }

        if self.is_html_mode.get():
            gui_settings["char_mode"] = self.select_char_mode.get_value()
            if self.is_need_text_string.get():
                gui_settings["text_string"] = self.set_text_string.get_value()
            elif self.is_asci_char_mode.get():
                gui_settings["asci_bright_mode"] = self.select_asci_mode.get_value()
                gui_settings["asci_shift"] = int(self.set_asci_shift_spinbox.get_value())
            gui_settings["output_path"] = asksaveasfilename(filetypes=[("Html file", ".html")],
                                                            defaultextension=".html")
        else:
            gui_settings["output_path"] = asksaveasfilename(filetypes=[("Image files", ".png")],
                                                            defaultextension=".png")

        gui_settings["color_mode"] = self.select_color_mode.get_value()
        if self.is_8_bit_mode.get():
            gui_settings["eight_bit_color_mode"] = self.select_8_bit_mode.get_value()

        # Todo covert settings from Tkinter to default settings format
        # Set settings
        settings = Settings()
        settings.gui_mode_set_settings(gui_settings)
        # Main logic
        my_image = MyImage(settings)
        # Format and display data
        PresentData(my_image, settings)
