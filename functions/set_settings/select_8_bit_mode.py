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
        if CHOSE == '1' or CHOSE == "low red" or CHOSE == "":
            ACTION = "low_red"
        elif CHOSE == '2' or CHOSE == "low green":
            ACTION = "low_green"
        elif CHOSE == '3' or CHOSE == "low blue":
            ACTION = "low_blue"
        else:
            print("Wrong option try again")
            continue

        return ACTION
