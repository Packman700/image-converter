from procedures.PhotoAverageRgbList import PhotoAverageRgbList
from procedures.ChangeColorMode import ChangeColorMode

class MyImage:
    def __init__(self, settings):
        self.photo_rgb_list = PhotoAverageRgbList(settings).get_data()
        self.photo_rgb_list = ChangeColorMode(self.photo_rgb_list, settings).get_data()
