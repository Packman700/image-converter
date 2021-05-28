MENU = """     SELECT MODE
---------------------
1. Next characters
2. Random characters
3. Asci characters
---------------------"""

def select_char_mode():
    while True:
        print(MENU)

        CHOSE = input('You\'r chose: ').lower().strip()

        CHAR_MODE = ''
        if CHOSE == '1' or CHOSE == "next characters" or CHOSE == "":
            CHAR_MODE = "next_characters"  # mode 2
        elif CHOSE == '2' or CHOSE == "random characters":
            CHAR_MODE = "random_characters"  # mode 1
        elif CHOSE == '3' or CHOSE == "asci characters":
            CHAR_MODE = "asci_characters"  # mode 3
        else:
            print("Wrong option try again")
            continue

        return CHAR_MODE