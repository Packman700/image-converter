def set_asci_shift(ASCI_BRIGHT_MODE):
    while True:
        ASCI_SHIFT = 0

        try:
            if ASCI_BRIGHT_MODE == "10_grey_level":
                ASCI_SHIFT = float(input("Set shift between -0 to 10: "))
                if not 0 <= ASCI_SHIFT <= 10:
                    print("Shift must be between 0 and 10 try again")
                    continue
            elif ASCI_BRIGHT_MODE == "70_grey_level":
                ASCI_SHIFT = float(input("Set shift between 0 to 70: "))
                if not 0 <= ASCI_SHIFT <= 70:
                    print("Shift must be between 0 and 70 try again")
                    continue
        except (TypeError, ValueError):
            print("You must write number")

        if ASCI_SHIFT % 1 != 0:
            print("ASCI_SHIFT must be integer")
            continue

        return int(ASCI_SHIFT)
