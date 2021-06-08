from tkinter import *

class GenerateFileButton(Frame):
    def __init__(self, parent, command, text, is_enable):
        super().__init__(parent)
        # Set variables
        self.is_enable = is_enable

        # Create variables listeners
        self.is_enable.trace("w", self.is_enable_trace)

        # Create widgets
        self.button = Button(self, command=command, text=text, state=DISABLED)

        # Print widgets
        self.button.pack()

    # Listeners
    def is_enable_trace(self, *args):
        self.button.config(state=(NORMAL if self.is_enable.get() else DISABLED))