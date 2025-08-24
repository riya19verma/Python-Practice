import tkinter
# Code to add widgets will go here...
s_welcome = tkinter.Tk()
window = tkinter.W()

s_welcome.title("FRAIL TRAILS")
tkinter.GROOVE
lbl1 = tkinter.Label(window, text="WELCOME DOG LOVERS", font=("Arial Bold", 25))
lbl1.Grid(column=5, row=2)
lbl2 = tkinter.Label(window, text="To the world of Street Dogs", font=("Arial Bold", 25))
lbl2.Grid(column=3, row=4)
lbl3 = tkinter.Label(window, text="Please Enter your Mobile Number", font=("Arial Bold", 20))
lbl3.Grid(column=5, row=5)
lbl4 = tkinter.Label(window, text="\n \n \n Note : I agree to the Terms and Conditions and privacy policy", font=("Arial Bold", 12))
lbl4.Grid(column=2, row=10)

s_welcome.mainloop()
