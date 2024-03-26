from tkinter import *
root = Tk()

root.title("Testing Screen")

computer = Label(root, bg="Blue", fg="White", text="Computer", font=("Times", 60, "bold"))
science = Label(root, bg="Green", fg="Yellow", text="Science", font=("Ariel", 76, "bold"))
cool = Label(root, bg="Purple", fg="Black", text="Is Cool", font=("Times", 70, "bold"))

computer.pack(fill=Y, side=LEFT)
science.pack(fill=Y, side=RIGHT)
cool.pack(fill=Y)

root.mainloop()