import tkinter.messagebox
from PIL import ImageTk, Image
from tkinter import *
import mysql.connector as sqlcon
import random as rd  # may be used

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

def update1():
    #Updating Location Master - Area, PIN, etc later on base data shall come from MCD
    global pin,e43,e44,e45,e46,e47
    p41=pin
    p43=e43.get()
    p44=e44.get()
    p45=e45.get()
    p46=e46.get()
    p47=e47.get()
    print("pin-",pin, p43, p44,p45, p46,p47)
    query='update locmaster set feedingpoint="{}",feedercount="{}",foodpots="{}",waterpots="{}",milkpots="{}" where pincode="{}"'.format(p43,p44,p45,p46,p47,pin)
    cur.execute(query)
    con.commit()
    
    tkinter.messagebox.showinfo("Done", "You have been successfuly updated location details")


def exitsession(r):
    exitprg='N'
    tkinter.messagebox.showinfo("Closing sessions", "This shall terminate the program")
    exitlbl=Label(root1,text="Do you want to exit, entrer Y",font='arial 14 bold')
    exitprg=tkinter.Entry(r)
    if exitprg=='Y':
        exit()
    

# for Registration of dog lovers
def register():
    global e1,e2,e3,e4,e5,e6,e7,e8
    root1=Tk()
 
    label1=Label(root1,text="FRAIL TRAILS\n",font='Times 30 bold ')
    label1.pack(side=TOP, padx=0, pady=0)
    label2=Label(root1,text="Welcome Dog Lovers",font='Times 30 bold')
    label2.pack(side=TOP, padx=0, pady=0)
    label3=Label(root1,text="REGISTER YOURSELF",font='arial 16 bold')
    label3.pack(side=TOP, padx=0, pady=0)

    #label4.place(x=30,y=130)
    frame=Frame(root1,height=700,width=200)
    frame.pack()

    #Labels and data entry area 

    l1=Label(root1,text="Mobile #",font='arial 14 bold')
    l1.place(x=230,y=190)
    e1=tkinter.Entry(root1)
    e1.place(x=560,y=190)
    l2=Label(root1,text="Name ",font='arial 14 bold')
    l2.place(x=230,y=230)
    e2=tkinter.Entry(root1)
    e2.place(x=560,y=230)
    l3=Label(root1,text="eMAIL Id",font='arial 14 bold')
    l3.place(x=230,y=270)
    e3=tkinter.Entry(root1)
    e3.place(x=560,y=270)
    l4=Label(root1,text="Will feed street dogs",font='arial 14 bold')
    l4.place(x=230,y=310)
    e4=tkinter.Entry(root1)
    e4.place(x=560,y=310)
    l5=Label(root1,text="Are you a Vet Doctor ",font='arial 14 bold')
    l5.place(x=230,y=350)
    e5=tkinter.Entry(root1)
    e5.place(x=560,y=350)
    l6=Label(root1,text="Can you Provide Funds",font='arial 14 bold')
    l6.place(x=230,y=390)
    e6=tkinter.Entry(root1)
    e6.place(x=560,y=390)
    l7=Label(root1,text="Can you Invest Time",font='arial 14 bold')
    l7.place(x=230,y=430)
    e7=tkinter.Entry(root1)
    e7.place(x=560,y=430)
    l8=Label(root1,text="Any Suggestions",font='arial 14 bold')
    l8.place(x=230,y=470)
    e8=tkinter.Entry(root1)
    e8.place(x=560,y=470)

    
    b1=Button(root1,text="SUBMIT",command=entry1)
    b1.place(x=600,y=600)

    root.resizable(False, False)
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


# for Find data about Locations short of pots
def searchloc():
    global s1, pin
    root3=Tk()
    label1=Label(root3,text="FRAIL TRAILS\n",font='Times 30 bold ')
    label1.pack(side=TOP, padx=0, pady=1)
    frame=Frame(root3,height=500,width=200)
    frame.pack()
    label2=Label(root3,text="Search Location Details",font='arial 24 bold')
    label2.place(x=30,y=35)

    l31=Label(root3,text="PIN Code ",font='arial 14 bold')
    l31.place(x=130,y=190)
    s1=tkinter.Entry(root3)
    s1.place(x=360,y=190)
    pin=s1.get()
    msg=""
    b31=Button(root3,text='Search',command=view_data)
    b31.place(x=400,y=260)
    
    root.resizable(False, False)
    root3.mainloop()

def view_data():
    global v1,msg
    v1=s1.get()
    sq='select pincode,feedercount,foodpots,waterpots,milkpots from locmaster where pincode=%s'
    cur.execute(sq,[v1])
    sqr=cur.fetchall()
    l=list(sqr)
    for i in sqr:
        flg=0
        msg="Status of area:"
        if i[1]==0:
            msg=msg+"no feeders\n"
            flg=1
        if i[2]==0:
            msg=msg+"No foodpots\n"
            flg=1
        if i[3]==0:
            msg=msg+"No water pots\n"
            flg=1
        if i[4]==0:
            msg=msg+"No Milk pots\n"
            flg=1
        if flg==0:
            msg=msg+"sufficient resources"

        tkinter.messagebox.showinfo("Status of Area: "+i[0],msg)
            

    


# for Mofify details
def addlocdet():
    global s1, pin
    root4=Tk()
    label1=Label(root4,text="FRAIL TRAILS\n",font='Times 30 bold ')
    label1.pack(side=TOP, padx=0, pady=1)
    frame=Frame(root4,height=500,width=600)
    frame.pack()
    label2=Label(root4,text="Search Location Details For Modification",font='arial 24 bold')
    label2.place(x=30,y=35)

    l31=Label(root4,text="PIN Code ",font='arial 14 bold')
    l31.place(x=130,y=190)
    s1=tkinter.Entry(root4)
    s1.place(x=360,y=190)
    pin=s1.get()
    b41=Button(root4,text='Modify Data',command=modify_data)
    b41.place(x=400,y=260)
    
    root.resizable(False, False)
    root4.mainloop()

def modify_data():
    global v1,msg,e41,e43,e44,e45,e46,e47,pin

    v1=s1.get()
    sq='select pincode,feedingpoint,feedercount,foodpots,waterpots,milkpots from locmaster where pincode=%s'
    cur.execute(sq,[v1])
    sqr=cur.fetchall()
    i=list(sqr)

    root41=Tk()
    label1=Label(root41,text="FRAIL TRAILS\n",font='Times 30 bold ')
    label1.pack(side=TOP, padx=0, pady=0)
    lbl12="MODIFY LOCATION DATA FOR THE PIN CODE"+pin+"\n"
    label2=Label(root41,text=lbl12,font='Times 30 bold ')
    label2.pack(side=TOP, padx=0, pady=0)

    frame=Frame(root41,height=500,width=200)
    frame.pack()
    
    for i in sqr:
        print(i)
        e41=i[0]
        lbl43='Is this MCD Feeding point('+i[1]+')'
        l43=Label(root41,text=lbl43,font='arial 14 bold')
        l43.place(x=100,y=250)
        e43=tkinter.Entry(root41)
        e43.place(x=460,y=250)
        lbl44='Enter count of Feeders as of now('+str(i[2])+")"
        l44=Label(root41,text=lbl44,font='arial 14 bold')
        l44.place(x=100,y=330)
        e44=tkinter.Entry(root41)
        e44.place(x=460,y=330)
        lbl45='Enter number of Food Pots('+str(i[3])+')'
        l45=Label(root41,text=lbl45,font='arial 14 bold')
        l45.place(x=100,y=370)
        e45=tkinter.Entry(root41)
        e45.place(x=460,y=370)
        lbl46="Enter number of Water Pots("+str(i[4])+")"
        l46=Label(root41,text=lbl46,font='arial 14 bold')
        l46.place(x=100,y=410)
        e46=tkinter.Entry(root41)
        e46.place(x=460,y=410)
        lbl47="Enter number of Milk Pots("+str(i[5])+")"
        l47=Label(root41,text=lbl47,font='arial 14 bold')
        l47.place(x=100,y=450)
        e47=tkinter.Entry(root41)
        #e47.insert(0,i[5])
        e47.place(x=460,y=450)

        pin=i[0]
        b41=Button(root41,text="SUBMIT",command=update1)
        b41.place(x=300,y=550)
        exit

    root.resizable(True, True)
    root41.mainloop()
            



# View T&C for onboarding
def termscond():
    
    root5=Tk()
    label51=Label(root5,text="FRAIL TRAILS\n",font='Times 30 bold ')
    label51.pack(side=TOP, padx=0, pady=0)
    lbl52="This is Prototype for Stray Dogs Feeders Platform.\n The copytright for this platform are with Riya Verma. \n The users are not supposed to copy and reproduce this idea"
    label52=Label(root5,text=lbl52,font='arial 14 bold')
    label52.pack(side=TOP,padx=0, pady=100)

    frame=Frame(root5,height=500,width=200)
    frame.pack()
    #T&C File fetch and display
    
    root.resizable(False, False)
    root5.mainloop()


root=Tk()
photo = PhotoImage(file = r"C:\Users\Dell\Desktop\LOGO.png")
img_label = Label(image = photo)
b=Button(root,image = photo,command=None,borderwidth = 0)
b.pack(side=TOP, padx=0, pady=0)
#
label=Label(root,text="FRAIL TRAILS",font='Times 40 bold')
label.pack(side=TOP, padx=0, pady=0)
label2=Label(root,text="Welcome Dog Lovers\n",font='Times 30 bold')
label2.pack(side=TOP, padx=0, pady=0)
label3=Label(root,text="To the World of Street Dogs\n",font='Times 16 bold')
label3.pack(side=TOP, padx=0, pady=5)
#
reg_but = PhotoImage(file = 'C:\\Users\\Dell\\Desktop\\Slide1.png')
img_label1 = Label(image = reg_but)
b1=Button(root,image = reg_but,command=register,borderwidth = 0)
b1.pack(side=TOP, padx=0, pady=0)
#
loc_mas = PhotoImage(file = 'C:\\Users\\Dell\\Desktop\\Slide2.png')
img_label2 = Label(image = loc_mas)
b2=Button(root,image = loc_mas,command=locmaster,borderwidth = 0)
b2.pack(side=TOP, padx=0, pady=0)
#
srch = PhotoImage(file = 'C:\\Users\\Dell\\Desktop\\Slide3.png')
img_label3 = Label(image = loc_mas)
b3=Button(root,image = srch,command=searchloc,borderwidth = 0)
b3.pack(side=TOP,padx=0, pady=0)
#
add_det = PhotoImage(file = 'C:\\Users\\Dell\\Desktop\\Slide41.png')
img_label4 = Label(image = add_det)
b4=Button(root,image = add_det,command=addlocdet,borderwidth = 0)
b4.pack(side=TOP, padx=0, pady=0)
#
t_a_c = PhotoImage(file = 'C:\\Users\\Dell\\Desktop\\Slide5.png')
img_label5 = Label(image = t_a_c)
b5=Button(root,image=t_a_c,command=termscond,borderwidth = 0)
b5.pack(side=TOP, padx=0, pady=0)
label.pack()
frame=Frame(root,height=555, width=595)
frame.pack()
root.resizable(True,True)
root.mainloop()
