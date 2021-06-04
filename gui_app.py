from procedures.Settings import Settings
from MyImage import MyImage
from procedures.PresentData import PresentData

from gui.App import App
from tkinter import Tk
from tkinter.filedialog import (asksaveasfilename)

IMG_FORMATS = ".png .bmp .gif .jpg .jpeg .tff .tiff .eps"

def main_logic():
    # Todo add check if user fill all fields

    # Todo Add simple if to use proper format
    output_filename = asksaveasfilename(filetypes=[("Html file", ".html")], defaultextension=".html")
    output_filename = asksaveasfilename(filetypes=[("Image files", IMG_FORMATS)], defaultextension=".jpg")

    # Todo covert settings from Tkinter to default settings format
    # Set settings
    settings = Settings()
    settings.gui_mode_set_settings()
    # Main logic
    my_image = MyImage(settings)
    # Format and display data
    PresentData(my_image, settings)

# Main loop
window = Tk()
App(main_logic)
window.mainloop()
