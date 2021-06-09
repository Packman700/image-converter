from tkinter import *

class MyLabelFrame(Frame):
    def __init__(self, parent, text_label):
        super().__init__(parent)
        self.label_frame = LabelFrame(self, text=text_label)
        self.label_frame.pack()

    def get(self):
        return self.label_frame
