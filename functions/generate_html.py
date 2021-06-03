import random

def return_span_tag(rgb_color, char):
    return f'<span style="color:rgb({",".join(str(e) for e in rgb_color)})">{char}</span>'

def char_generator(string):
    while True:
        for char in string:
            yield char

def return_random_char_from_string(string):
    return random.choice(string)

def asci_generator(color, settings):
    asci_chars = []
    if settings.asci_bright_mode == "70_grey_level":
        asci_chars = list(" .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")
    elif settings.asci_bright_mode == "10_grey_level":
        asci_chars = list(" .:-=+*#%@")
    elif settings.asci_bright_mode == "reverse_70_grey_level":
        asci_chars = list(" .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")
        asci_chars.reverse()
    elif settings.asci_bright_mode == "reverse_10_grey_level":
        asci_chars = list(" .:-=+*#%@")
        asci_chars.reverse()

    brightest_color = max(color)

    char_index = round(brightest_color/255*len(asci_chars)) - settings.asci_shift

    # BUG FIX
    if char_index >= len(asci_chars):
        char_index = len(asci_chars) - 1

    return asci_chars[char_index]
