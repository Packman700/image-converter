from PIL import Image
import math
import random
from html_page_template import HTML_TEMPLATE

### FUNCTIONS ###
def convert_to_2d_array(input_list, row_size):
    output_list = []
    for i in range(len(input_list)//row_size):
        start_index = i * row_size
        output_list.append(list(input_list[start_index: start_index + row_size]))
    return output_list


def calculate_correction(photo_width, row_size):
    MAX_CORRECTION_VALUE = 2.8
    correction_rate = (photo_width / row_size) % 1
    return correction_rate * MAX_CORRECTION_VALUE

def return_span_tag(rgb_color, char):
    return f'<span style="color:rgb({",".join(str(e) for e in rgb_color)})">{char}</span>'

def char_generator(string):
    while True:
        for char in string:
            yield char

def return_random_char_from_string(string):
    return random.choice(string)
### SETTINGS ###
# SETUP
ROW_SIZE = 50
TEXT_STRING = "10"
CHAR_MODE = "random_characters"  # mode 1
# CHAR_MODE = "next_characters"  # mode 2

COLOR_MODE = "rgb"  # mode 1
# COLOR_MODE = "gray_scale"  # mode 2

image = Image.open("MonaLisa.jpg")

img_width = image.width
img_height = image.height

COLUMN_SIZE = round((img_height * ROW_SIZE) / img_width)

img_rgb_2d_list = convert_to_2d_array(list(image.getdata()), img_width)  # TAKE DATA FROM PICTURE
average_rgb_values_2d_list = []

# PIXEL SIZE RATIO
char_pixel_size = img_width / ROW_SIZE
COLOR_CORRECTION = calculate_correction(img_width, ROW_SIZE)
CHAR_PIXEL_FIELD = char_pixel_size**2 - COLOR_CORRECTION  # alis number of pixels

### MAIN LOGIC ###
for x in range(COLUMN_SIZE):
    x_start_index = math.floor(x * char_pixel_size)
    rows = img_rgb_2d_list[x_start_index: math.floor(x_start_index + char_pixel_size)]
    for y in range(ROW_SIZE):
        y_start_index = math.floor(y * char_pixel_size)

        # COUNT AVERAGE PIXEL SIZE VALUES
        char_color = [0, 0, 0]
        for row in rows:
            pixels_values = row[y_start_index: math.floor(y_start_index + char_pixel_size)]
            sum_rgb = [sum(rgb) for rgb in zip(*pixels_values)]
            char_color = [char_color[0] + sum_rgb[0],
                          char_color[1] + sum_rgb[1],
                          char_color[2] + sum_rgb[2]]

        # DIVIDE EVERY RGB VALUE BY NUMBER OF PIXELS
        char_color = (round(char_color[0]/CHAR_PIXEL_FIELD),
                      round(char_color[1]/CHAR_PIXEL_FIELD),
                      round(char_color[2]/CHAR_PIXEL_FIELD))

        average_rgb_values_2d_list.append(char_color)


### PRINT & DATA INTERPRETATION ###
# CREATE PIXELATED IMAGE
new_image = Image.new(mode="RGB", size=(ROW_SIZE, COLUMN_SIZE))
# if COLOR_MODE == "rgb":
#     pass
# elif COLOR_MODE == "gray_scale":
#     pass
new_image.putdata(average_rgb_values_2d_list)
new_image.save('pixelated_photo.png')

# CREATE HTML FILE
styled_spans = ""
char_gen = char_generator(TEXT_STRING)
with open("pixelated_photo.html", "w") as file:
    current_char = None
    for i in range(1, ROW_SIZE * COLUMN_SIZE):
        if CHAR_MODE == "next_characters":
            current_char = next(char_gen)
        elif CHAR_MODE == "random_characters":
            current_char = return_random_char_from_string(TEXT_STRING)

        styled_spans += return_span_tag(average_rgb_values_2d_list[i], current_char)

        if i % ROW_SIZE == 0 and i != 0:
            styled_spans += "\n"

    file.write(HTML_TEMPLATE.format(styled_spans))

