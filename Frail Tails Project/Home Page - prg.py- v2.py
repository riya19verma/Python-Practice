import tkinter.messagebox
from PIL import ImageTk, Image
from tkinter import *
import mysql.connector as sqlcon
import random as rd  # may be used

# https://cbsepython.in/hospital-management-system-using-mysql-connectivity-and-tkinter-gui-python-project/
#connection
con = sqlcon.connect(host="localhost",user="root",password="Flat@162")
cur = con.cursor()
cur = con.cursor(buffered=True)
if (con):
    # Carry out normal procedure
    print ("DB connection successful")
else :
    print ("Error 01 : Connection unsuccessful")

cur.execute("create database if not exists STRAYDOG")
cur.execute("use STRAYDOG")
cur.execute("create table if not exists RUser"
            "("
            "mobileno char(10) primary key,"
            "name char(50),"
            "emailId char(30),"
            "isfeeder char(1),"
            "isVetDoc char(1),"
            "isFundDoner char(1),"
            "isVetCare char(1),"
            "remarks varchar(200))")
cur.execute("create table if not exists LocMaster"
            "("
            "pincode char(6) primary key,"
            "areaname char(30),"
            "feedingpoint char(1),"
            "latlong varchar(15),"
            "feedercount int,"
            "foodpots int,"
            "waterpots int,"
            "milkpots int)")

#Registration of User
def entry1():
    #registration of dog lovers - feeders, money donors, helping hands etc
     #NOT UPDATING PROPERLY
    global e1,e2,e3,e4,e5,e6,e7,e8
    p1=e1.get()
    p2=e2.get()
    p3=e3.get()
    p4=e4.get()
    p5=e5.get()
    p6=e6.get()
    p7=e7.get()
    p8=e8.get()

    query='insert into RUser values("{}","{}","{}","{}","{}","{}","{}","{}")'.format(p1,p2,p3,p4,p5,p6,p7,p8)
    cur.execute(query)
    con.commit()

    tkinter.messagebox.showinfo("Done", "You have been successfuly registered")

def entry2():
    #Feeding Location Master - Area, PIN, etc later on base data shall come from MCD
    #NOT UPDATING PROPERLY
    global e21,e22,e23,e24,e25,e26,e27,e28
    p21=e21.get()
    p22=e22.get()
    p23=e23.get()
    p24=e24.get()
    p25=e25.get()
    p26=e26.get()
    p27=e27.get()
    p28=e28.get()

    query='insert into locmaster values("{}","{}","{}","{}","{}","{}","{}","{}")'.format(p21,p22,p23,p24,p25,p26,p27,p28)
    cur.execute(query)
    con.commit()

    tkinter.messagebox.showinfo("Done", "You have been successfuly entered location details")

def exitsession(r):
    exitprg='N'
    #Feeding Location Master - Area, PIN, etc later on base data shall come from MCD
    tkinter.messagebox.showinfo("Closing sessions", "This shall terminate the program")
    exitlbl=Label(root1,text="Do you want to exit, entrer Y",font='arial 14 bold')
    exitprg=tkinter.Entry(r)
    if exitprg=='Y':
        exit()
    

# for Registration
def register():
    global e1,e2,e3,e4,e5,e6,e7,e8
    root1=Tk()
    #Change
    photo = PhotoImage(file = r"C:\Users\Dell\Desktop\slide1.png")
    label1=Label(root1,text="FRAIL TRAILS\n",font='Times 30 bold ')
    label1.pack(side=TOP, padx=0, pady=0)
    label2=Label(root1,text="Welcome Dog Lovers\n",font='Times 30 bold')
    label2.pack(side=TOP, padx=0, pady=1)
    label3=Label(root1,text="To the World of Street Dogs\n",font='Times 16 bold')
    #CHANGES HERE 
    label3.pack(side=TOP, padx=0, pady=1)
    label4=Label(root1,text="REGISTER YOURSELF\n",font='arial 16 bold')
    label4.place(x=30,y=130)
    frame=Frame(root1,height=700,width=200)
    frame.pack()
    l1=Label(root1,text="Mobile #",font='arial 14 bold')
    l1.place(x=130,y=190)
    e1=tkinter.Entry(root1)
    e1.place(x=460,y=190)
    l2=Label(root1,text="Name ",font='arial 14 bold')
    l2.place(x=130,y=230)
    e2=tkinter.Entry(root1)
    e2.place(x=460,y=230)
    l3=Label(root1,text="eMAIL Id",font='arial 14 bold')
    l3.place(x=130,y=270)
    e3=tkinter.Entry(root1)
    e3.place(x=460,y=270)
    l4=Label(root1,text="Will feed street dogs",font='arial 14 bold')
    l4.place(x=130,y=310)
    e4=tkinter.Entry(root1)
    e4.place(x=460,y=310)
    l5=Label(root1,text="Are you a Vet Doctor ",font='arial 14 bold')
    l5.place(x=130,y=350)
    e5=tkinter.Entry(root1)
    e5.place(x=460,y=350)
    l6=Label(root1,text="Can you Provide Funds",font='arial 14 bold')
    l6.place(x=130,y=390)
    e6=tkinter.Entry(root1)
    e6.place(x=460,y=390)
    l7=Label(root1,text="Can you Invest Time",font='arial 14 bold')
    l7.place(x=130,y=430)
    e7=tkinter.Entry(root1)
    e7.place(x=460,y=430)
    l8=Label(root1,text="Any Suggestions",font='arial 14 bold')
    l8.place(x=130,y=470)
    e8=tkinter.Entry(root1)
    e8.place(x=460,y=470)

    
    b1=Button(root1,text="SUBMIT",command=entry1)
    b1.place(x=400,y=550)

    root.resizable(True, True)
    root1.mainloop()

# for Location Master and Stray Dogs Mapping
def locmaster():
    global e21,e22,e23,e24,e25,e26,e27,e28
    root2=Tk()
    label1=Label(root2,text="FRAIL TRAILS\n",font='Times 30 bold ')
    label1.pack(side=TOP, padx=0, pady=0)
    frame=Frame(root2,height=500,width=200)
    frame.pack()
    label4=Label(root2,text="ENTER LOCATION DETAILS",font='arial 20 bold')
    label4.place(x=30,y=130)
    l21=Label(root2,text="Pin Code",font='arial 14 bold')
    l21.place(x=130,y=170)
    e21=tkinter.Entry(root2)
    e21.place(x=460,y=170)
    l22=Label(root2,text="Area Name",font='arial 14 bold')
    l22.place(x=130,y=210)
    e22=tkinter.Entry(root2)
    e22.place(x=460,y=210)
    l23=Label(root2,text="Is this MCD Feeding point",font='arial 14 bold')
    l23.place(x=130,y=250)
    e23=tkinter.Entry(root2)
    e23.place(x=460,y=250)
    l24=Label(root2,text="Enter Lat Long of the point",font='arial 14 bold')
    l24.place(x=130,y=290)
    e24=tkinter.Entry(root2)
    e24.place(x=460,y=290)
    l25=Label(root2,text="Enter count of Feeders as of now",font='arial 14 bold')
    l25.place(x=130,y=330)
    e25=tkinter.Entry(root2)
    e25.place(x=460,y=330)
    l26=Label(root2,text="Enter number of Food Pots",font='arial 14 bold')
    l26.place(x=130,y=370)
    e26=tkinter.Entry(root2)
    e26.place(x=460,y=370)
    l27=Label(root2,text="Enter number of Water Pots",font='arial 14 bold')
    l27.place(x=130,y=410)
    e27=tkinter.Entry(root2)
    e27.place(x=460,y=410)
    l28=Label(root2,text="Enter number of Milk Pots",font='arial 14 bold')
    l28.place(x=130,y=450)
    e28=tkinter.Entry(root2)
    e28.place(x=460,y=450)


    b1=Button(root2,text="SUBMIT",command=entry2)
    b1.place(x=100,y=500)

    root.resizable(True, True)
    root2.mainloop()


# for Registration
def searchloc():
    global e1,e2,e3,e4,e5,e6
    root1=Tk()
    label1=Label(root1,text="FRAIL TRAILS\n",font='Times 30 bold ')
    label1.pack(side=TOP, padx=0, pady=1)
    frame=Frame(root1,height=500,width=200)
    frame.pack()
    label2=Label(root1,text="Welcome Dog Lovers",font='arial 24 bold')
    label2.place(x=30,y=35)
    label3=Label(root1,text="To the World of Street Dogs",font='arial 24 bold')
    label3.place(x=30,y=50)
    label4=Label(root1,text="REGISTER YOURSELF",font='arial 20 bold')
    label4.place(x=30,y=65)
    l1=Label(root1,text="Mobile #",font='arial 20 bold')
    l1.place(x=30,y=90)
    e1=tkinter.Entry(root1)
    e1.place(x=60,y=90)
    l2=Label(root1,text="eMAIL Id",font='arial 20 bold')
    l2.place(x=30,y=110)
    e2=tkinter.Entry(root1)
    e2.place(x=60,y=110)
    l3=Label(root1,text="Are you a Vet Doctor",font='arial 20 bold')
    l3.place(x=30,y=130)
    e3=tkinter.Entry(root1)
    e3.place(x=60,y=130)
    l4=Label(root1,text="Can you Provide Funds",font='arial 20 bold')
    l4.place(x=30,y=150)
    e4=tkinter.Entry(root1)
    e4.place(x=60,y=150)
    l5=Label(root1,text="Can you Invest Time",font='arial 20 bold')
    l5.place(x=30,y=170)
    e5=tkinter.Entry(root1)
    e5.place(x=60,y=170)
    l6=Label(root1,text="Any Suggestions",font='arial 20 bold')
    l6.place(x=30,y=190)
    e6=tkinter.Entry(root1)
    e6.place(x=60,y=190)
    b1=Button(root1,text="SUBMIT",command=entry)
    b1.place(x=100,y=250)

    root.resizable(False, False)
    root1.mainloop()


# for Registration
def addlocdet():
    global e1,e2,e3,e4,e5,e6
    root1=Tk()
    label1=Label(root1,text="FRAIL TRAILS\n",font='Times 30 bold ')
    label1.pack(side=TOP, padx=0, pady=1)
    frame=Frame(root1,height=500,width=200)
    frame.pack()
    label2=Label(root1,text="Welcome Dog Lovers",font='arial 24 bold')
    label2.place(x=30,y=35)
    label3=Label(root1,text="To the World of Street Dogs",font='arial 24 bold')
    label3.place(x=30,y=50)
    label4=Label(root1,text="REGISTER YOURSELF",font='arial 20 bold')
    label4.place(x=30,y=65)
    l1=Label(root1,text="Mobile #",font='arial 20 bold')
    l1.place(x=30,y=90)
    e1=tkinter.Entry(root1)
    e1.place(x=60,y=90)
    l2=Label(root1,text="eMAIL Id",font='arial 20 bold')
    l2.place(x=30,y=110)
    e2=tkinter.Entry(root1)
    e2.place(x=60,y=110)
    l3=Label(root1,text="Are you a Vet Doctor",font='arial 20 bold')
    l3.place(x=30,y=130)
    e3=tkinter.Entry(root1)
    e3.place(x=60,y=130)
    l4=Label(root1,text="Can you Provide Funds",font='arial 20 bold')
    l4.place(x=30,y=150)
    e4=tkinter.Entry(root1)
    e4.place(x=60,y=150)
    l5=Label(root1,text="Can you Invest Time",font='arial 20 bold')
    l5.place(x=30,y=170)
    e5=tkinter.Entry(root1)
    e5.place(x=60,y=170)
    l6=Label(root1,text="Any Suggestions",font='arial 20 bold')
    l6.place(x=30,y=190)
    e6=tkinter.Entry(root1)
    e6.place(x=60,y=190)
    b1=Button(root1,text="SUBMIT",command=entry)
    b1.place(x=100,y=250)

    root.resizable(False, False)
    root1.mainloop()

# View T&C for onboarding
def termscond():
    global e1,e2,e3,e4,e5,e6
    root1=Tk()
    label1=Label(root2,text="FRAIL TRAILS\n",font='Times 30 bold ')
    label1.pack(side=TOP, padx=0, pady=0)
    frame=Frame(root1,height=500,width=200)
    frame.pack()
    #T&C File fetch and display
    
    root.resizable(False, False)
    root1.mainloop()

def update_clock(self):
    now = time.strftime("%H:%M:%S")
    self.label.configure(text=now)
    self.after(1000, self.update_clock)

    root.resizable(False, False)
    root1.mainloop()


root=Tk()
label=Label(root,text="FRAIL TRAILS",font='Times 40 bold')
label.pack(side=TOP, padx=0, pady=10)
label2=Label(root,text="Welcome Dog Lovers\n",font='Times 30 bold')
label2.pack(side=TOP, padx=0, pady=0)
label3=Label(root,text="To the World of Street Dogs\n",font='Times 16 bold')
label3.pack(side=TOP, padx=0, pady=0)
b1=Button(text="User \nRegistration",font="helvetica 20 bold",bg="white",command=register)
b2=Button(text="Stray \nLocation Master",font="helvetica 20 bold",bg="white",command=locmaster)
b3=Button(text="Search \nLocations",font="helvetica 20 bold",bg="white",command=searchloc)
b4=Button(text="Add \nDetails",font="helvetica 20 bold",bg="white",command=addlocdet)
b5=Button(text="Terms & \nConditions",font="helvetica 20 bold",bg="white",command=termscond)
label.pack()

b1.pack(side=LEFT,padx=50)
b2.pack(side=LEFT,padx=50)
b3.pack(side=LEFT,padx=50)
b4.pack(side=LEFT,padx=50)
b5.pack(side=LEFT,padx=50)

frame=Frame(root,height=700, width=170)
frame.pack()
root.resizable(False,False)
root.mainloop()
