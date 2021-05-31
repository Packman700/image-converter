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
        if CHOSE in ('1', 'rgb', ''):
            CHAR_MODE = "rgb"
        elif CHOSE in ('2', 'gray scale'):
            CHAR_MODE = "gray_scale"
        elif CHOSE in ('3', '8 bit'):
            CHAR_MODE = "8_bit"
        else:
            print("Wrong option try again")
            continue

        return CHAR_MODE
