from html_page_template import HTML_TEMPLATE
from functions import generate_html

def generate_HTML_file(average_rgb_values_2d_list, settings):
    styled_spans = ""
    char_gen = generate_html.char_generator(settings.text_string)
    with open(f"{settings.current_path}/pixelated_photo.html", "w") as file:
        current_char = None
        for i in range(1, settings.row_size * settings.column_size):
            current_color = average_rgb_values_2d_list[i]
            if settings.char_mode == "next_characters":
                current_char = next(char_gen)
            elif settings.char_mode == "random_characters":
                current_char = generate_html.return_random_char_from_string(settings.text_string)
            elif settings.char_mode == "asci_characters":
                current_char = generate_html.asci_generator(current_color, settings)
                # current_color = (255,255,255)
            styled_spans += generate_html.return_span_tag(current_color, current_char)

            if i % settings.row_size == 0 and i != 0:
                styled_spans += "\n"

        file.write(HTML_TEMPLATE.format(styled_spans))
