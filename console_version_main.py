from procedures.Settings import Settings
from MyImage import MyImage
from procedures.PresentData import PresentData

# Set settings
settings = Settings().text_mode_set_settings()
# Main logic
my_image = MyImage(settings)
# Format and display data
PresentData(my_image, settings)
