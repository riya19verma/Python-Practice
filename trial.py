from tkinter import *

root = Tk()
frm = Frame(root, padx=100, pady=100)
frm.grid()

# Create a label with width and height in characters/lines
label = Label(frm, text="Hello World!", width=20, height=5, bg="lightblue")
label.grid(column=0, row=0)

root.mainloop()
