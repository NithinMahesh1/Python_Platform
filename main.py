import tkinter as tk
import nueron
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

img = Image.open("Jarvis3.png")
photo = ImageTk.PhotoImage(img)


def jarvisButtonClick():
    # TODO this will be where we pass in values to the nueron
    print("clicked")
    nueron.node()


button = tk.Button(image=photo, height=100, width=100, command=jarvisButtonClick, text="ok")
button.pack()

root.mainloop()