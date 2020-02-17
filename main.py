import tkinter as tk
import nueron
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

img = Image.open("Jarvis3.png")
photo = ImageTk.PhotoImage(img)


def jarvisButtonClick():
    # TODO this will be where we pass in values to the nueron

    print("Select from Program List: ")
    print("training")
    print("testing")
    print("run node")
    print("Hit 'q' to exit")
    print("")
    askUser = input("Select what program: ")


    if askUser == "training":
        nueron.trainingSet()

    if askUser == "testing":
        nueron.testingSet()

    if askUser == "run node":
        nueron.node()

    if askUser == "q":
        print("termination in progress... ")
        exit()

button = tk.Button(image=photo, height=100, width=100, command=jarvisButtonClick, text="ok")
button.pack()

root.mainloop()