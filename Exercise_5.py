from tkinter import *
root = Tk()

root.title("Testing Screen")
root.minsize(600, 400)

red = Label(root, bg="Red", fg="White", text="Red", font=("Ariel", 40, "bold"))
blue = Label(root, bg="Blue", fg="White", text="Blue", font=("Ariel", 40, "bold"))
green = Label(root, bg="Green", fg="White", text="Green", font=("Ariel", 40, "bold"))

red.pack(side=RIGHT, fill=BOTH, padx= 30, pady=30, expand=YES)
blue.pack(side=LEFT, fill=Y)
green.pack(side=BOTTOM, fill=X)
root.mainloop()