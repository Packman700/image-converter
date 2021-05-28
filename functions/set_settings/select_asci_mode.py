MENU = """  SELECT ASCI MODE
---------------------
1. 10 grey level
2. 70 grey level
---------------------"""

def select_asci_mode():
    while True:
        print(MENU)

        CHOSE = input('You\'r chose: ').lower().strip()

        MODE = ''
        if CHOSE == '1' or CHOSE == "10 grey level" or CHOSE == "":
            MODE = "10_grey_level"  # mode 2
        elif CHOSE == '2' or CHOSE == "70 grey level":
            MODE = "70_grey_level"  # mode 1
        else:
            print("Wrong option try again")
            continue

        return MODE
