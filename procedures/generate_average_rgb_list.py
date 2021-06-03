from PIL import Image
from functions import pixel_manipulation

def generate_average_rgb_list(settings):
    img_width = settings.image.width
    img_height = settings.image.height

    char_pixel_size = img_width / settings.row_size

    # Calculate CHAR_PIXEL_FIELD
    COLOR_CORRECTION = pixel_manipulation.calculate_correction(img_width, settings.row_size)
    CHAR_PIXEL_FIELD = char_pixel_size**2 - COLOR_CORRECTION  # approximate number of pixels

    img_rgb_2d_list = pixel_manipulation.convert_to_2d_array(list(settings.image.getdata()), img_width)  # TAKE DATA FROM PICTURE

    average_rgb_values_2d_list = pixel_manipulation.return_average_rgb_values_2d_list(img_rgb_2d_list,
                                                                                      settings.column_size,
                                                                                      settings.row_size,
                                                                                      CHAR_PIXEL_FIELD,
                                                                                      char_pixel_size)
    return average_rgb_values_2d_list
