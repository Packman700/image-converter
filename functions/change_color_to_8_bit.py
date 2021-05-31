def change_color_to_8_bit(color, EIGHT_BIT_MODE):
    # Example 8 bit color
    # RRRGGGBB
    # 10110111
    ONE_BIT_RED = None
    ONE_BIT_GREEN = None
    ONE_BIT_BLUE = None
    if EIGHT_BIT_MODE == "low_blue":
        ONE_BIT_RED = 255 / 3
        ONE_BIT_GREEN = 255 / 3
        ONE_BIT_BLUE = 255 / 2
    elif EIGHT_BIT_MODE == "low_green":
        ONE_BIT_RED = 255 / 3
        ONE_BIT_GREEN = 255 / 2
        ONE_BIT_BLUE = 255 / 3
    elif EIGHT_BIT_MODE == "low_red":
        ONE_BIT_RED = 255 / 2
        ONE_BIT_GREEN = 255 / 3
        ONE_BIT_BLUE = 255 / 3

    [R, G, B] = color

    R = int(round(round(R/ONE_BIT_RED) * ONE_BIT_RED))
    G = int(round(round(G/ONE_BIT_GREEN) * ONE_BIT_GREEN))
    B = int(round(round(G/ONE_BIT_BLUE) * ONE_BIT_BLUE))

    return (R, G, B)
