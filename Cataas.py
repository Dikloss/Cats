from tkinter import *
from PIL import Image,ImageTk
import requests
from io import BytesIO

from pygame.examples.cursors import image

window = Tk()
window.title("Cats")
window.geometry("600x480")

label = Label()
label.pack()

url = "https://cataas.com/cat"
img = load_image(url)

if img:
    label.config(image=img)

window.mainloop()


