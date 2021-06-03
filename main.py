from procedures.Settings import Settings
from MyImage import MyImage
from procedures.PresentData import PresentData

### SETTINGS ###
# SETUP
settings = Settings()
my_image = MyImage(settings)
PresentData(my_image, settings)
