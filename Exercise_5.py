from tkinter import *
root = Tk()

root.title("Testing Screen")

red = Label(root, bg="Red", fg="White", text="red", font=("Ariel", 40, "bold"))
blue = Label(root, bg="Blue", fg="White", text="Blue", font=("Ariel", 40, "bold"))
green = Label(root, bg="Green", fg="White", text="Green", font=("Ariel", 40, "bold"))

red.pack(expand=YES)
blue.pack(fill=X, side=BOTTOM)
green
root.mainloop()