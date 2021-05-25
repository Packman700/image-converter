import random

def return_span_tag(rgb_color, char):
    return f'<span style="color:rgb({",".join(str(e) for e in rgb_color)})">{char}</span>'

def char_generator(string):
    while True:
        for char in string:
            yield char

def return_random_char_from_string(string):
    return random.choice(string)

def asci_generator(color, ASCI_SHIFT, ASCI_BRIGHT_MODE):
    ASCI_CHARS = []
    if ASCI_BRIGHT_MODE == "70_grey_level":
        ASCI_CHARS = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    elif ASCI_BRIGHT_MODE == "10_grey_level":
        ASCI_CHARS = list(" .:-=+*#%@")

    brightest_color = max(color)

    char_index = round(brightest_color/255*len(ASCI_CHARS)) - ASCI_SHIFT

    return ASCI_CHARS[char_index]