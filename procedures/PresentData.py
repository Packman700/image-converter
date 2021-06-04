from PIL import Image
from HTML_PAGE_TEMPLATE import HTML_TEMPLATE
from procedures.CharServices import CharServices

class PresentData:
    # output_file_name = "pixelated_photo"

    def __init__(self, my_image, settings):
        self.char_services = CharServices()
        if settings.action == "pixelated_image":
            self.generate_img_file(my_image.photo_rgb_list, settings)
        elif settings.action == "generate_HTML_file":
            self.generate_html_file(my_image.photo_rgb_list, settings)

    def generate_html_file(self, photo_rgb_list, settings):
        styled_spans = ""
        char_gen = self.char_services.char_generator(settings.text_string)
        with open(settings.output_path, "w") as file:
            current_char = None
            for i in range(1, settings.row_size * settings.column_size):
                current_color = photo_rgb_list[i]

                if settings.char_mode == "next_characters":
                    current_char = next(char_gen)
                elif settings.char_mode == "random_characters":
                    current_char = self.char_services.return_random_char_from_string(settings.text_string)
                elif settings.char_mode == "asci_characters":
                    current_char = self.char_services.asci_generator(current_color, settings)

                styled_spans += self.char_services.return_span_tag(current_color, current_char)

                if i % settings.row_size == 0 and i != 0:
                    styled_spans += "\n"

            file.write(HTML_TEMPLATE.format(styled_spans))

    def generate_img_file(self, my_image, settings):
        new_image = Image.new(mode="RGB", size=(settings.row_size, settings.column_size))
        new_image.putdata(my_image)
        new_image.save(settings.output_path)
