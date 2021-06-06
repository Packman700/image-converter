from tkinter import *
from operator import methodcaller

class RadioButtons(Frame):
    def __init__(self, parent, options, text_label, is_enable):
        super().__init__(parent)

        # Set variables
        self.is_enable = is_enable
        self.chosen_option = StringVar(None, list(options.values())[0])
        self.radio_buttons = []

        # Create variables listeners
        self.is_enable.trace('w', self.is_enable_trace)

        # Create widgets
        label = Label(self, text=text_label)
        for (name, value) in options.items():
            button = Radiobutton(self, value=value, text=name, variable=self.chosen_option,
                                 state=DISABLED)
            self.radio_buttons.append(button)

        # Print widgets
        label.pack()
        list(map(lambda button: button.pack(), self.radio_buttons))

    # Listeners
    def is_enable_trace(self, *args):
        for button in self.radio_buttons:
            print(button)
            button.config(state=(NORMAL if self.is_enable.get() else DISABLED))

    # Other
    def get(self):
        return self.chosen_option.get()
