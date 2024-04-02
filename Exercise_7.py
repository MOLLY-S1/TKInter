from tkinter import *


def comment(stuff):
    label_text.set(stuff)


root = Tk
root.minsize(300, 50)
text = StringVar()
root.title("NUMBERS")

label_text = StringVar()
message = Label(root, textvariable=label_text, font=("Times", 24, "Bold"))
message.pack()

