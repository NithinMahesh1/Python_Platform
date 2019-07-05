import tkinter as tk
import jarvis
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

img = Image.open("Jarvis3.png")
photo = ImageTk.PhotoImage(img)


def jarvisButtonClick():
    print("clicked")
    jarvis.testing()


button = tk.Button(image=photo, height=100, width=100, command=jarvisButtonClick, text="ok")
button.pack()

root.mainloop()