# import os.path
from PIL import Image

def chose_image():
    while True:
        path = input("Write path to photo: ")

        # if not os.path.isfile("path"):
        #     print("I can't find file try again")
        #     continue

        try:
          img = Image.open(path)
          img.verify() #I perform also verify, don't know if he sees other types o defects
          img.close() #reload is necessary in my case
        except:
            print("Sorry something go wrong try again")
            continue

        return path
