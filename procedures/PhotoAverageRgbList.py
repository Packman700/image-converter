import math

class PhotoAverageRgbList:
    def __init__(self, settings):
        img_width = settings.image.width
        char_pixel_size = img_width / settings.row_size

        bright_correction = self._calculate_bright_correction(img_width, settings.row_size)
        char_pixel_field = char_pixel_size ** 2 - bright_correction  # approximate number of pixels

        img_rgb_2d_list = self._convert_to_2d_array(list(settings.image.getdata()), img_width)  # TAKE DATA FROM PICTURE

        self.average_rgb_values = self._return_average_rgb_values_list(img_rgb_2d_list, settings, char_pixel_field, char_pixel_size)

    def get_data(self):
        return self.average_rgb_values

    @staticmethod
    def _calculate_bright_correction(img_width, row_size):
        MAX_CORRECTION_VALUE = 2.8
        correction_rate = (img_width / row_size) % 1
        return correction_rate * MAX_CORRECTION_VALUE

    @staticmethod
    def _convert_to_2d_array(input_list, row_size):
        output_list = []
        for i in range(len(input_list) // row_size):
            start_index = i * row_size
            output_list.append(list(input_list[start_index: start_index + row_size]))
        return output_list

    @staticmethod
    def _return_average_rgb_values_list(img_rgb_2d_list, settings, char_pixel_field, char_pixel_size):
        return_average_rgb_values = []
        for x in range(settings.column_size):
            x_start_index = math.floor(x * char_pixel_size)
            rows = img_rgb_2d_list[x_start_index: math.floor(x_start_index + char_pixel_size)]
            for y in range(settings.row_size):
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
                char_color = (round(char_color[0] / char_pixel_field),
                              round(char_color[1] / char_pixel_field),
                              round(char_color[2] / char_pixel_field))

                return_average_rgb_values.append(char_color)

        return return_average_rgb_values
