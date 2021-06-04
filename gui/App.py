from tkinter import *
from .SelectPhotoButton import SelectPhotoButton

class App(Frame):
    source_path = image = row_size = action = char_mode = text_string = asci_bright_mode = asci_shift \
        = color_mode = eight_bit_color_mode = column_size = output_path = None

    def __init__(self, main_logic):
        super().__init__()
        self.pack()

        self.select_photo_button = SelectPhotoButton(self)
        self.select_photo_button.pack()
        self.select_photo_button.get_string_var().trace("r", self.update_photo_path_callback)

        # Just a tests
        self.test_btn = Button(self, text='test', state=DISABLED)
        self.test_btn.pack()

    def update_photo_path_callback(self, *args):
        if self.select_photo_button.get_value():
            self.test_btn["state"] = NORMAL
        else:
            self.test_btn["state"] = DISABLED
        self.source_path = self.select_photo_button.get_value()


