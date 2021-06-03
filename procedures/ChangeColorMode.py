class ChangeColorMode:
    changed_photo_rgb_list = None

    def __init__(self, photo_rgb_list, settings):
        if settings.color_mode == "rgb":
            self.changed_photo_rgb_list = photo_rgb_list
        elif settings.color_mode == "gray_scale":
            self.changed_photo_rgb_list = list(map(lambda rgb: (max(rgb), max(rgb), max(rgb)), photo_rgb_list))
        elif settings.color_mode == "8_bit":
            self.changed_photo_rgb_list = list(
                map(lambda rgb: self._change_color_to_8_bit(rgb, settings.eight_bit_color_mode),
                    photo_rgb_list))
        else:
            raise Exception("You chose invalid color mode")

    @staticmethod
    def _change_color_to_8_bit(color, eight_bit_mode):
        """
        Example 8 bit color
        RRRGGGBB
        10110111
        """
        new_red = new_green = new_blue = None
        if eight_bit_mode == "low_blue":
            new_red = 255 / 3
            new_green = 255 / 3
            new_blue = 255 / 2
        elif eight_bit_mode == "low_green":
            new_red = 255 / 3
            new_green = 255 / 2
            new_blue = 255 / 3
        elif eight_bit_mode == "low_red":
            new_red = 255 / 2
            new_green = 255 / 3
            new_blue = 255 / 3

        [R, G, B] = color

        R = int(round(round(R / new_red) * new_red))
        G = int(round(round(G / new_green) * new_green))
        B = int(round(round(G / new_blue) * new_blue))

        return R, G, B

    def get_data(self):
        return self.changed_photo_rgb_list
