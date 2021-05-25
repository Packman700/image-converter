from PIL import Image

def generate_img_file(average_rgb_values_2d_list, SETTINGS):
    new_image = Image.new(mode="RGB", size=(SETTINGS["ROW_SIZE"], SETTINGS["COLUMN_SIZE"]))
    new_image.putdata(average_rgb_values_2d_list)
    new_image.save(f'{SETTINGS["PATH"]}/pixelated_photop.png')