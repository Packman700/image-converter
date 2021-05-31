MENU = """  SELECT ASCI MODE
---------------------
1. 10 grey level
1. Reverse 10 grey level
3. 70 grey level
4. Reverse 70 grey level
---------------------"""

def select_asci_mode():
    while True:
        print(MENU)

        CHOSE = input('You\'r chose: ').lower().strip()

        MODE = ''
        if CHOSE == '1' or CHOSE == "10 grey level" or CHOSE == "":
            MODE = "10_grey_level"
        elif CHOSE == '2' or CHOSE == "reverse 10 grey level":
            MODE = "reverse_10_grey_level"
        elif CHOSE == '3' or CHOSE == "70 grey level":
            MODE = "70_grey_level"
        elif CHOSE == '4' or CHOSE == "reverse 70 grey level":
            MODE = "reverse_70_grey_level"
        else:
            print("Wrong option try again")
            continue

        return MODE
