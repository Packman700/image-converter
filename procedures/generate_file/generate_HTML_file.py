from html_page_template import HTML_TEMPLATE
from functions import generate_html

def generate_HTML_file(average_rgb_values_2d_list, TEXT_STRING, CHAR_MODE, ROW_SIZE, COLUMN_SIZE, path):
    styled_spans = ""
    char_gen = generate_html.char_generator(TEXT_STRING)
    with open(f"{path}/pixelated_photo.html", "w") as file:
        current_char = None
        for i in range(1, ROW_SIZE * COLUMN_SIZE):
            if CHAR_MODE == "next_characters":
                current_char = next(char_gen)
            elif CHAR_MODE == "random_characters":
                current_char = generate_html.return_random_char_from_string(TEXT_STRING)

            styled_spans += generate_html.return_span_tag(average_rgb_values_2d_list[i], current_char)

            if i % ROW_SIZE == 0 and i != 0:
                styled_spans += "\n"

        file.write(HTML_TEMPLATE.format(styled_spans))
