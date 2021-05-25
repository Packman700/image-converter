from html_page_template import HTML_TEMPLATE
from functions import generate_html

def generate_HTML_file(average_rgb_values_2d_list, SETTINGS):
    styled_spans = ""
    char_gen = generate_html.char_generator(SETTINGS["TEXT_STRING"])
    with open(f"{SETTINGS['PATH']}/pixelated_photo.html", "w") as file:
        current_char = None
        for i in range(1, SETTINGS["ROW_SIZE"] * SETTINGS["COLUMN_SIZE"]):
            current_color = average_rgb_values_2d_list[i]
            if SETTINGS["CHAR_MODE"] == "next_characters":
                current_char = next(char_gen)
            elif SETTINGS["CHAR_MODE"] == "random_characters":
                current_char = generate_html.return_random_char_from_string(SETTINGS["TEXT_STRING"])
            elif SETTINGS["CHAR_MODE"] == "asci_characters":
                current_char = generate_html.asci_generator(current_color,
                                                            SETTINGS["ASCI_SETTINGS"])
                # current_color = (255,255,255)
            styled_spans += generate_html.return_span_tag(current_color, current_char)

            if i % SETTINGS["ROW_SIZE"] == 0 and i != 0:
                styled_spans += "\n"

        file.write(HTML_TEMPLATE.format(styled_spans))
