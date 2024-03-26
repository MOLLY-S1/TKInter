from tkinter import *
root = Tk()
root.title("APPLE!")

# Create a reference to the image
apple_image = PhotoImage(file="apple_3.png")

# Placing the image onto a label
image_label = Label(root, image=apple_image)
image_label.pack()

# Adding text beneath
label_text = Label(root, bg="Red", fg="White", text="This is an apple", font=("Times", 60, "bold"))
label_text.pack()

root.mainloop()