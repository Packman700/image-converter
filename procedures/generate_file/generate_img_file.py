from PIL import Image

def generate_img_file(average_rgb_values_2d_list, settings):
    new_image = Image.new(mode="RGB", size=(settings.row_size, settings.column_size))
    new_image.putdata(average_rgb_values_2d_list)
    new_image.save(f'{settings.current_path}/pixelated_photop.png')
