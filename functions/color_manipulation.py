def change_color_mode(average_rgb_values_2d_list, COLOR_MODE):
    if COLOR_MODE == "rgb":
        return average_rgb_values_2d_list
    elif COLOR_MODE == "gray_scale":
        return list(map(lambda rgb: (max(rgb), max(rgb), max(rgb)), average_rgb_values_2d_list))