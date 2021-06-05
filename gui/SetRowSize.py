from tkinter import *
from PIL import Image


class SetRowSize(Frame):
    def __init__(self, parent, photo_path):
        super().__init__(parent)

        self.photo_path = photo_path
        self.photo_path.trace("r", self.update_photo_path_callback)

        self.max_value = IntVar()
        validate_spinbox_value = self.register(self.validate_input)

        self.row_value = StringVar()
        self.row_size_spinbox = Spinbox(self, from_=1, to=1,
                                        validate="key", validatecommand=(validate_spinbox_value, "%P"),
                                        textvariable=self.row_value,
                                        state=DISABLED)
        self.row_size_spinbox.grid(row=0, column=1)

        self.label = Label(self, text="Chose output width: ")
        self.label.grid(row=0, column=0)

    def update_photo_path_callback(self, *args):
        if self.photo_path.get():
            width = Image.open(self.photo_path.get()).width
            self.max_value.set(width)
            self.row_size_spinbox.config(to=self.max_value.get(), state=NORMAL)
        else:
            self.row_size_spinbox.config(to=1, state=DISABLED)

    def validate_input(self, new_value, *args):
        if new_value.isdigit():
            # Prevention for first char equal 0 in two digit number
            if len(new_value) > 1 and new_value[0] == '0':
                self.row_value.set(new_value[1:])
                # If we don't redefine validate property, this method will not called again ;>
                self.row_size_spinbox.config(validate="key")
                return False

            # Prevention for type to big number
            if int(new_value) > self.max_value.get():
                self.row_value.set(self.max_value.get())
                self.row_size_spinbox.config(validate="key")
                return False
            return True

        elif new_value == "":
            self.row_value.set(0)
            self.row_size_spinbox.config(validate="key")
            return False
        else:
            return False

    def get(self):
        return self.row_size_spinbox.get()
