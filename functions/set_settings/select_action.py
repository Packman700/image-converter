MENU = """     SELECT MODE
---------------------
1. Generate HTML file
2. Pixelated image
---------------------"""

def select_action():
    while True:
        print(MENU)

        CHOSE = input('You\'r chose: ').lower().strip()

        ACTION = ''
        if CHOSE == '1' or CHOSE == "generate HTML file" or CHOSE == "":
            ACTION = "generate_HTML_file"  # mode 2
        elif CHOSE == '2' or CHOSE == "pixelated image":
            ACTION = "pixelated_image"  # mode 1
        else:
            print("Wrong option try again")
            continue

        return ACTION