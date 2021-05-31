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

        if CHOSE in ('1', "10 grey level", ""):
            MODE = "10_grey_level"
        elif CHOSE in ('2', "reverse 10 grey level"):
            MODE = "reverse_10_grey_level"
        elif CHOSE in ('3', "70 grey level"):
            MODE = "70_grey_level"
        elif CHOSE in ('4', "reverse 70 grey level"):
            MODE = "reverse_70_grey_level"

        else:
            print("Wrong option try again")
            continue

        return MODE
