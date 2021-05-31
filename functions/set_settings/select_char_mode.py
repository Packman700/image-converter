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
        if CHOSE in ('1', 'next characters', ''):
            CHAR_MODE = "next_characters"  # mode 2
        elif CHOOSE in ('2', 'random characters'):
            CHAR_MODE = "random_characters"  # mode 1
        elif CHOSE in ('3', 'asci characters'):
            CHAR_MODE = "asci_characters"  # mode 3
        else:
            print("Wrong option try again")
            continue

        return CHAR_MODE
