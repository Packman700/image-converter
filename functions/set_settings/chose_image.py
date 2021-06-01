# import os.path
from PIL import Image

def chose_image():
    while True:
        path = input("Write path to photo: ")

        try:
          img = Image.open(path)
          img.verify() #I perform also verify, don't know if he sees other types o defects
          img.close() #reload is necessary in my case
        except FileNotFoundError:
            print("File not found")
            continue
        except Image.UnidentifiedImageError:
            print("Selected file isn't image")
            continue

        return path
