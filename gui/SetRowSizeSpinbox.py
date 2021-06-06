from tkinter import *
from PIL import Image

class SetRowSize(Frame):
    def __init__(self, parent, photo_path, is_enable):
        super().__init__(parent)

        # Set variables
        self.photo_path = photo_path
        self.is_enable = is_enable
        self.max_value = IntVar()
        self.row_value = StringVar()

        # Create variables listeners
        self.photo_path.trace("w", self.photo_path_trace)
        self.is_enable.trace('w', self.is_enable_trace)

        # Create widgets
        validate_spinbox_value = self.register(self.validate_input)
        self.row_size_spinbox = Spinbox(self, from_=1, to=1,
                                        validate="key", validatecommand=(validate_spinbox_value, "%P"),
                                        textvariable=self.row_value,
                                        state=DISABLED)

        self.label = Label(self, text="Chose output width: ")

        # Print widgets
        self.row_size_spinbox.grid(row=0, column=1)
        self.label.grid(row=0, column=0)

    # Listeners
    def photo_path_trace(self, *args):
        if self.photo_path.get():
            width = Image.open(self.photo_path.get()).width
            self.max_value.set(width)
            self.row_size_spinbox.config(to=self.max_value.get())
        else:
            self.row_size_spinbox.config(to=1)

    def is_enable_trace(self, *args):
        self.row_size_spinbox.config(state=(NORMAL if self.is_enable.get() else DISABLED))

    # Register functions
    def validate_input(self, new_value, *args):
        if new_value.isdigit():
            # Prevention for type to big number
            if int(new_value) > self.max_value.get():
                self.row_value.set(self.max_value.get())
                self.row_size_spinbox.config(validate="key")
                return False
            return True
        elif new_value == "":
            self.row_value.set(1)
            self.row_size_spinbox.config(validate="key")
            return False
        else:
            return False

    # Other
    def get(self):
        return self.row_size_spinbox.get()
