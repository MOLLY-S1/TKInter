from tkinter import *


def count_up():
    global number
    number += 1
    print(number)


def count_down():
    global number
    number -= 1
    print(number)


root = Tk()
number = 0
root.title("COUNTING")
root.minsize(300, 50)

button_1 = Button(root, text="Count Up", command=count_up)
button_1.pack()
button_2 = Button(root, text="Count Down", command=count_down)
button_2.pack()

root.mainloop()