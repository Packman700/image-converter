from PIL import Image
from functions import pixel_manipulation

def generate_average_rgb_list(image, ROW_SIZE, COLUMN_SIZE):
    img_width = image.width
    img_height = image.height

    char_pixel_size = img_width / ROW_SIZE

    # Calculate CHAR_PIXEL_FIELD
    COLOR_CORRECTION = pixel_manipulation.calculate_correction(img_width, ROW_SIZE)
    CHAR_PIXEL_FIELD = char_pixel_size**2 - COLOR_CORRECTION  # approximate number of pixels

    img_rgb_2d_list = pixel_manipulation.convert_to_2d_array(list(image.getdata()), img_width)  # TAKE DATA FROM PICTURE

    average_rgb_values_2d_list = pixel_manipulation.return_average_rgb_values_2d_list(img_rgb_2d_list,
                                                                                      COLUMN_SIZE,
                                                                                      ROW_SIZE,
                                                                                      CHAR_PIXEL_FIELD,
                                                                                      char_pixel_size)
    return average_rgb_values_2d_list