def set_row_size(image_width):
    while True:
        try:
            ROW_SIZE = float(input(f"Chose row size (value between 1 to {image_width}: "))
        except ValueError:
            print("You must write number")
            continue

        if ROW_SIZE > image_width:
            print("Row size cant be bigger than photo")
            continue
        elif ROW_SIZE < 1:
            print("Row size cant be smaller than 1")
            continue
        elif ROW_SIZE % 1 != 0:
            print("Row size must be integer")
            continue

        return int(ROW_SIZE)
