from PIL import Image
import math

def convert_to_2d_array(input_list, row_size):
    output_list = []
    for i in range(len(input_list)//row_size):
        start_index = i * row_size
        output_list.append(list(input_list[start_index: start_index + row_size]))
    return output_list

ROW_SIZE = 10
TEXT_STRING = "#"
image = Image.open("Sprite-0001.png")
# image = Image.open("landscape.png")

img_width = image.width
img_height = image.height

COLUMN_SIZE = round((img_height * ROW_SIZE) / img_width)
char_pixel_size = img_height / ROW_SIZE

img_rgb_2d_list = convert_to_2d_array(list(image.getdata()), img_width)

# print(COLUMN_SIZE)
# print(ROW_SIZE)

average_rgb_values_2d_list = []
CHAR_PIXEL_FIELD = char_pixel_size**2
for x in range(ROW_SIZE):
    x_start_index = math.floor(x * char_pixel_size)
    rows = img_rgb_2d_list[x_start_index : math.floor(x_start_index + char_pixel_size)]
    for y in range(COLUMN_SIZE):
        print(rows)
        y_start_index = math.floor(y * char_pixel_size)

        char_color = [0, 0, 0]
        for row in rows:
            row_values = row[y_start_index: math.floor(y_start_index + char_pixel_size)]
            # print(row_values)
            divided_rgb_list = map(lambda rgb: (rgb[0]/CHAR_PIXEL_FIELD, rgb[1]/CHAR_PIXEL_FIELD, rgb[2]/CHAR_PIXEL_FIELD),
                                   row_values)
            sum_rgb = [sum(rgb) for rgb in zip(*divided_rgb_list)]
            char_color = [char_color[0] + sum_rgb[0], char_color[1] + sum_rgb[1], char_color[2] + sum_rgb[2]]

        char_color = (round(char_color[0]), round(char_color[1]), round(char_color[2]))
        average_rgb_values_2d_list.append(char_color)

new_image = Image.new(mode = "RGB", size = (ROW_SIZE, COLUMN_SIZE))
new_image.putdata(average_rgb_values_2d_list)
new_image.save('test.png')
# print(img_rgb_2d_list)
# print(char_pixel_size)

# image.show()