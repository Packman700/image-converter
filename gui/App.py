from tkinter import *
from .ChoosePhotoButton import ChoosePhotoButton
from .SetRowSize import SetRowSize

class App(Frame):
    source_path = image = row_size = action = char_mode = text_string = asci_bright_mode = asci_shift \
        = color_mode = eight_bit_color_mode = column_size = output_path = None

    def __init__(self, main_logic):
        super().__init__()
        self.pack()

        self.choose_photo_button = ChoosePhotoButton(self)
        self.choose_photo_button.pack()
        self.choose_photo_button.get().trace("r", self.update_photo_path_callback)

        self.set_row_size_spinbox = SetRowSize(self, self.choose_photo_button.get())
        self.set_row_size_spinbox.pack()

        # Just a tests
        self.test_btn = Button(self, text='test', state=DISABLED, command=lambda : print(self.set_row_size_spinbox.get()))
        self.test_btn.pack()

    def update_photo_path_callback(self, *args):
        if self.choose_photo_button.get_value():
            self.test_btn["state"] = NORMAL
        else:
            self.test_btn["state"] = DISABLED
        self.source_path = self.choose_photo_button.get_value()


