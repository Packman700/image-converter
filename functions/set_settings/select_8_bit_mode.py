MENU = """  SELECT 8 BIT MODE
---------------------
1. Low red
2. Low green
3. Low blue
---------------------"""


def select_8_bit_mode():
    while True:
        print(MENU)

        CHOSE = input('You\'r chose: ').lower().strip()

        ACTION = ''
        if CHOSE in ('1', 'low red', ''):
            ACTION = "low_red"
        elif CHOSE in ('2', 'low green'):
            ACTION = "low_green"
        elif CHOSE in ('3', 'low blue'):
            ACTION = "low_blue"
        else:
            print("Wrong option try again")
            continue

        return ACTION
