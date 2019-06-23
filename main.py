from tkinter import *

root = Tk()

topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

button1 = Button(topframe, text="Submit", fg="red")
button2 = Button(topframe, text="Next", fg="blue")

button1.pack(side=RIGHT)
button2.pack(side=LEFT)

root.mainloop()