from PIL import Image

def generate_img_file(average_rgb_values_2d_list, ROW_SIZE, COLUMN_SIZE, path):
    new_image = Image.new(mode="RGB", size=(ROW_SIZE, COLUMN_SIZE))
    new_image.putdata(average_rgb_values_2d_list)
    new_image.save(f'{path}/pixelated_photop.png')