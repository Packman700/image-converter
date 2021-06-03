from functions.change_color_to_8_bit import *

def change_color_mode(average_rgb_values_2d_list, settings):
    if settings.color_mode == "rgb":
        return average_rgb_values_2d_list
    elif settings.color_mode == "gray_scale":
        return list(map(lambda rgb: (max(rgb), max(rgb), max(rgb)), average_rgb_values_2d_list))
    elif settings.color_mode == "8_bit":
        return list(map(lambda rgb: change_color_to_8_bit(rgb, settings.eight_bit_color_mode), average_rgb_values_2d_list))
    return average_rgb_values_2d_list
