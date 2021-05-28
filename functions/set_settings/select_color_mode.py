MENU = """ SELECT COLOR MODE
---------------------
1. rgb
2. gray scale
3. 8 bit
---------------------"""

def select_color_mode():
    while True:
        print(MENU)

        CHOSE = input('You\'r chose: ').lower().strip()

        CHAR_MODE = ''
        if CHOSE == '1' or CHOSE == "rgb" or CHOSE == "":
            CHAR_MODE = "rgb"
        elif CHOSE == '2' or CHOSE == "gray scale":
            CHAR_MODE = "gray_scale"
        elif CHOSE == '3' or CHOSE == "8 bit":
            CHAR_MODE = "8_bit"
        else:
            print("Wrong option try again")
            continue

        return CHAR_MODE
