from tkinter import *
from .ChoosePhotoButton import ChoosePhotoButton
from .SetRowSizeSpinbox import SetRowSize
from .RadioButtons import RadioButtons


class App(Frame):
    ACTION_OPTIONS = {"Generate HTML file": "generate_HTML_file",
                      "Pixelated image": "pixelated_image"}
    source_path = image = row_size = action = char_mode = text_string = asci_bright_mode = asci_shift \
        = color_mode = eight_bit_color_mode = column_size = output_path = None


    def __init__(self, main_logic):
        super().__init__()
        self.pack()

        # Set variables
        self.is_photo_chosen = BooleanVar(None, True)

        # Create widgets
        self.choose_photo_button = ChoosePhotoButton(self)
        self.select_action_radio_buttons = RadioButtons(self, self.ACTION_OPTIONS, "Select action",
                                                        self.is_photo_chosen)
        self.set_row_size_spinbox = SetRowSize(self, self.choose_photo_button.get(), self.is_photo_chosen)

        # Create widget variables listeners
        self.choose_photo_button.get().trace("r", self.update_photo_path_trace)

        # Print widgets
        self.choose_photo_button.pack()
        self.select_action_radio_buttons.pack()
        self.set_row_size_spinbox.pack()

        # Just a tests
        self.test_btn = Button(self, text='test', state=NORMAL, command=self.test)
        self.test_btn.pack()

    # Listeners
    def update_photo_path_trace(self, *args):
        if self.choose_photo_button.get_value():
            self.is_photo_chosen.set(True)
        else:
            self.is_photo_chosen.set(False)

    # Other
    def test(self):
        # print(self.is_photo_chosen.get())
        print(self.select_action_radio_buttons.get())
