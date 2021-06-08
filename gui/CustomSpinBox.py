from tkinter import *

class CustomSpinBox(Frame):
    def __init__(self, parent, max_value, min_value, label_text, is_enable):
        super().__init__(parent)

        # Set variables
        self.max_value = max_value
        self.is_enable = is_enable
        self.min_value = min_value
        self.row_value = StringVar()

        # Create variables listeners
        self.max_value.trace("w", self.max_value_trace)
        self.is_enable.trace('w', self.is_enable_trace)

        # Create widgets
        validate_spinbox_value = self.register(self.validate_input)
        self.spinbox = Spinbox(self, from_=self.min_value, to=self.min_value,
                               validate="key", validatecommand=(validate_spinbox_value, "%P"),
                               textvariable=self.row_value,
                               state=DISABLED)
        self.label = Label(self, text=label_text)

        # Print widgets
        self.spinbox.grid(row=0, column=1)
        self.label.grid(row=0, column=0)

    # Listeners
    def max_value_trace(self, *args):
        self.spinbox.config(to=self.max_value.get())
        self.spinbox.config(validate="key")

    def is_enable_trace(self, *args):
        self.spinbox.config(state=(NORMAL if self.is_enable.get() else DISABLED))

    # Register functions
    def validate_input(self, new_value, *args):
        if new_value.isdigit():
            if len(new_value) > 1 and new_value[0] == '0':
                self.row_value.set(new_value[1:])
                self.spinbox.config(validate="key")
                return False
            # Prevention for type to big number
            if int(new_value) > self.max_value.get():
                self.row_value.set(self.max_value.get())
                self.spinbox.config(validate="key")
                return False
            return True
        elif new_value == "":
            self.row_value.set(self.min_value)
            self.spinbox.config(validate="key")
            return False
        else:
            return False

    # Other
    def get(self):
        return self.spinbox

    def get_value(self):
        return self.spinbox.get()
