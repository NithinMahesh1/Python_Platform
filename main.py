from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

root = Tk()

img = Image.open("Jarvis3.png")
photo = ImageTk.PhotoImage(img)


def jarvisButtonClick(event):
    print("clicked")

button = tk.Button(image=photo, height=100, width=100, command=jarvisButtonClick, text="ok")
# button.config(relief=SUNKEN)
button.pack()

root.mainloop()