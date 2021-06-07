from tkinter import *

class SetTextString(Frame):
    def __init__(self, parent, text_label, is_enable):
        super().__init__(parent)

        # Set variables
        self.is_enable = is_enable
        self.text = StringVar()

        # Create variables listeners
        self.is_enable.trace('w', self.is_enable_trace)

        # Create widgets
        label = Label(self, text=text_label)
        self.text_widget = Entry(self, state=DISABLED)


        # Print widgets
        label.grid(row=0, column=0)
        self.text_widget.grid(row=0, column=1)
        # Listeners

    def is_enable_trace(self, *args):
        self.text_widget.config(state=(NORMAL if self.is_enable.get() else DISABLED))

        # Other

    def get(self):
        return self.text_widget

    def get_value(self):
        return self.text_widget.get()
