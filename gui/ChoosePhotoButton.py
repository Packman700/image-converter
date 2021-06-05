from tkinter import *
from tkinter.filedialog import askopenfilename

class ChoosePhotoButton(Frame):
    def __init__(self, parent, *kwargs, **args):
        super().__init__(parent, *kwargs, **args)

        button = Button(self, text="Chose File", command=self.select_file)
        button.pack()

        self.file_name = StringVar()

    def select_file(self):
        IMG_FORMATS = ".png .bmp .gif .jpg .jpeg .tff .tiff .eps"
        print(self.file_name.get())
        path_to_photo = askopenfilename(filetypes=[("Image files", IMG_FORMATS)])
        self.file_name.set(path_to_photo)
        print(self.file_name.get())

    def get_value(self):
        return self.file_name.get()

    def get(self):
        return self.file_name
