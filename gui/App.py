from tkinter import *
from .ChoosePhotoButton import ChoosePhotoButton
from .CustomSpinBox import CustomSpinBox
from .RadioButtons import RadioButtons
from options import OPTIONS
from .SetTextString import SetTextString
from PIL import Image

class App(Frame):
    source_path = image = width_size = action = char_mode = text_string = asci_bright_mode = asci_shift \
        = color_mode = eight_bit_color_mode = column_size = output_path = None

    def __init__(self, main_logic):
        super().__init__()
        self.pack()

        # Set variables
        self.is_photo_chosen = BooleanVar(None, False)
        self.is_html_mode = BooleanVar(None, False)
        self.is_need_text_string = BooleanVar(None, False)  # True if char_mode is random or next strings
        self.is_asci_char_mode = BooleanVar(None, False)
        self.is_8_bit_mode = BooleanVar(None, False)
        self.width_size = IntVar(None)

        # Create widgets
        self.choose_photo_button = ChoosePhotoButton(self)
        self.set_row_size_spinbox = CustomSpinBox(self, self.width_size, 1, "Chose output width: ", self.is_photo_chosen)
        self.select_action_radio = RadioButtons(self, OPTIONS["ACTION"], "Select action", self.is_photo_chosen)
        self.select_char_mode = RadioButtons(self, OPTIONS["CHAR_MODE"], "Select char mode", self.is_html_mode)
        self.set_text_string = SetTextString(self, "Entry text: ", self.is_need_text_string)
        self.select_asci_mode = RadioButtons(self, OPTIONS["ASCI_BRIGHT"], "Select asci mode", self.is_asci_char_mode)
        # self.set_asci_shift = SetAsciShift(self, self.is_asci_char_mode) # Todo add SetAsciShift class
        self.select_color_mode = RadioButtons(self, OPTIONS["COLOR_MODE"], "Select color mode", self.is_photo_chosen)
        self.select_8_bit_mode = RadioButtons(self, OPTIONS["8_BIT_COLOR"], "Select 8 bit mode", self.is_8_bit_mode)

        # Create widget variables listeners
        self.choose_photo_button.get().trace("wr", self.photo_path_trace)
        self.select_action_radio.get().trace("wr", self.select_action_radio_trace)
        self.select_char_mode.get().trace("wr", self.select_char_mode_trace)
        self.select_color_mode.get().trace("wr", self.select_color_mode_trace)

        # Print widgets
        self.choose_photo_button.pack()
        self.select_action_radio.pack()
        self.set_row_size_spinbox.pack()
        self.select_char_mode.pack()
        self.set_text_string.pack()
        self.select_asci_mode.pack()
        # self.set_asci_shift.pack()
        self.select_color_mode.pack()
        self.select_8_bit_mode.pack()

        # Just a tests
        self.test_btn = Button(self, text='test', state=NORMAL, command=self.test)
        self.test_btn.pack()

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

    # Other
    def test(self):
        # print(self.is_html_mode.get())
        print("Text string - ", self.is_need_text_string.get())
        print("Asci Char mode - ", self.is_asci_char_mode.get())
        print("8 bit mode - ", self.is_8_bit_mode.get())
        print("Text string - ", self.set_text_string.get_value())
        # print(self.select_action_radio_buttons.get())
