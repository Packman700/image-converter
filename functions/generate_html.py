import random

def return_span_tag(rgb_color, char):
    return f'<span style="color:rgb({",".join(str(e) for e in rgb_color)})">{char}</span>'

def char_generator(string):
    while True:
        for char in string:
            yield char

def return_random_char_from_string(string):
    return random.choice(string)

def asci_generator(color, ASCI_SETTINGS):
    ASCI_CHARS = []
    if ASCI_SETTINGS["ASCI_BRIGHT_MODE"] == "70_grey_level":
        ASCI_CHARS = list(" .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")
    elif ASCI_SETTINGS["ASCI_BRIGHT_MODE"] == "10_grey_level":
        ASCI_CHARS = list(" .:-=+*#%@")
    elif ASCI_SETTINGS["ASCI_BRIGHT_MODE"] == "reverse_70_grey_level":
        ASCI_CHARS = list(" .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")
        ASCI_CHARS.reverse()
    elif ASCI_SETTINGS["ASCI_BRIGHT_MODE"] == "reverse_10_grey_level":
        ASCI_CHARS = list(" .:-=+*#%@")
        ASCI_CHARS.reverse()

    brightest_color = max(color)

    char_index = round(brightest_color/255*len(ASCI_CHARS)) - ASCI_SETTINGS["ASCI_SHIFT"]

    # BUG FIX
    if char_index >= len(ASCI_CHARS):
        char_index = len(ASCI_CHARS) - 1

    return ASCI_CHARS[char_index]