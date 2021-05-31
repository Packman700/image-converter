MENU = """    SELECT ACTION
---------------------
1. Generate HTML file
2. Pixelated image
---------------------"""


def select_action():
    while True:
        print(MENU)

        CHOSE = input('You\'r chose: ').lower().strip()

        ACTION = ''
        if CHOSE in ('1', 'generate HTML file', ''):
            ACTION = "generate_HTML_file"  # mode 2
        elif CHOSE in ('2', 'pixelated image'):
            ACTION = "pixelated_image"  # mode 1
        else:
            print("Wrong option try again")
            continue

        return ACTION
