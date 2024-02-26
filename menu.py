# import tkinter as tk
# from tkinter import ttk
from tkinter import *


win = Tk()
win.geometry("1366x768")
win.resizable(0, 0)

labtitle = Label(
    text="Mitho Mitho Menu And Bill ",
    bg="skyblue",
    fg="white",
    font="aeriel 25 bold",
    padx=500,
)
labtitle.place(x=1, y=1)

imglogo = PhotoImage(
    file="C:\\Users\\Acer\\Desktop\\first_sem\\first_sem\\logoimage1.png"
)
lablogo = Label(image=imglogo)
lablogo.place(x=1, y=1)


frame1 = Frame(win, width=800, height=600, borderwidth=10, relief=GROOVE)
frame1.pack_propagate(False)
frame1.pack(side="left")

# label for food items
labfood = Label(
    frame1, text="Food Items", font="aeriel 15 bold", bg="blue", fg="white", padx=335
)
labfood.place(x=0, y=0)


# image 1 or chicken mo:mo
img1 = PhotoImage(file="C:\\Users\\Acer\\Desktop\\first_sem\\first_sem\\cmomo1.png")
l1 = Label(frame1, image=img1)
l1.place(x=50, y=30)

l2 = Label(frame1, text="Chicken mo:mo", font="aeriel 10 bold")
l2.place(x=45, y=130)

l3 = Label(frame1, text="Price:180", font="aeriel 10 bold")
l3.place(x=65, y=150)

my_spin1 = Spinbox(frame1, from_=0, to=10, width=4)
my_spin1.place(x=75, y=170)

# image 2 or veg mo:mo
img2 = PhotoImage(file="C:\\Users\\Acer\\Desktop\\first_sem\\first_sem\\vmomo1.png")
l4 = Label(frame1, image=img2)
l4.place(x=210, y=30)

l5 = Label(frame1, text="veg mo:mo", font="aeriel 10 bold")
l5.place(x=225, y=130)

l6 = Label(frame1, text="Price:120", font="aeriel 10 bold")
l6.place(x=230, y=150)

my_spin2 = Spinbox(frame1, from_=0, to=10, width=4)
my_spin2.place(x=240, y=170)

# image 3 or buff mo:mo
img3 = PhotoImage(file="C:\\Users\\Acer\\Desktop\\first_sem\\first_sem\\buffmomo1.png")
l7 = Label(frame1, image=img3)
l7.place(x=380, y=30)

l8 = Label(frame1, text="Buff mo:mo", font="aeriel 10 bold")
l8.place(x=390, y=130)

l9 = Label(frame1, text="Price:160", font="aeriel 10 bold")
l9.place(x=400, y=150)

my_spin3 = Spinbox(frame1, from_=0, to=10, width=4)
my_spin3.place(x=410, y=170)

# image 4 or paneer mo:mo
img4 = PhotoImage(
    file="C:\\Users\\Acer\\Desktop\\first_sem\\first_sem\\paneer momo1.png"
)
l10 = Label(frame1, image=img4)
l10.place(x=550, y=30)

l11 = Label(frame1, text="Paneer mo:mo", font="aeriel 10 bold")
l11.place(x=570, y=130)

l12 = Label(frame1, text="Price:140", font="aeriel 10 bold")
l12.place(x=580, y=150)

my_spin4 = Spinbox(frame1, from_=0, to=10, width=4)
my_spin4.place(x=590, y=170)

# iamge 5 or chicken pizza
img5 = PhotoImage(
    file="C:\\Users\\Acer\\Desktop\\first_sem\\first_sem\\chicken pizza1.png"
)
l13 = Label(frame1, image=img5)
l13.place(x=10, y=220)

l14 = Label(frame1, text="Chicken pizza", font="aeriel 10 bold")
l14.place(x=50, y=330)

l15 = Label(frame1, text="Price:350", font="aeriel 10 bold")
l15.place(x=70, y=350)

my_spin5 = Spinbox(frame1, from_=0, to=10, width=4)
my_spin5.place(x=80, y=370)

# image 6 or veg burger
img6 = PhotoImage(
    file="C:\\Users\\Acer\\Desktop\\first_sem\\first_sem\\veg burger1.png"
)
l16 = Label(frame1, image=img6)
l16.place(x=260, y=200)

l17 = Label(frame1, text="Veg burger", font="aeriel 10 bold")
l17.place(x=280, y=330)

l18 = Label(frame1, text="Price:220", font="aeriel 10 bold")
l18.place(x=285, y=350)

my_spin6 = Spinbox(frame1, from_=0, to=10, width=4)
my_spin6.place(x=300, y=370)

# image7 or buff sausage
img7 = PhotoImage(
    file="C:\\Users\\Acer\\Desktop\\first_sem\\first_sem\\buff sausage1.png"
)
l19 = Label(frame1, image=img7)
l19.place(x=430, y=220)

l20 = Label(frame1, text="Buff sausage", font="aeriel 10 bold")
l20.place(x=450, y=330)

l21 = Label(frame1, text="Price:50", font="aeriel 10 bold")
l21.place(x=460, y=350)

my_spin7 = Spinbox(frame1, from_=0, to=10, width=4)
my_spin7.place(x=470, y=370)

# image 8 or mutton sekuwa
img8 = PhotoImage(
    file="C:\\Users\\Acer\\Desktop\\first_sem\\first_sem\\mutton sekuwa1.png"
)
l22 = Label(frame1, image=img8)
l22.place(x=580, y=220)

l23 = Label(frame1, text="Mutton sekuwa", font="aeriel 10 bold")
l23.place(x=600, y=330)

l24 = Label(frame1, text="Price:200", font="aeriel 10 bold")
l24.place(x=610, y=350)

my_spin8 = Spinbox(frame1, from_=0, to=10, width=4)
my_spin8.place(x=620, y=370)

# label for soft drinks
labdrink = Label(
    frame1, text="Soft drinks", font="aeriel 15 bold", bg="green", fg="white", padx=335
)
labdrink.place(x=0, y=400)

# image 9 or cold drinks
img9 = PhotoImage(
    file="C:\\Users\\Acer\\Desktop\\first_sem\\first_sem\\cold drinks1.png"
)
l25 = Label(frame1, image=img9)
l25.place(x=30, y=450)

l26 = Label(frame1, text="Cold drinks", font="aeriel 10 bold")
l26.place(x=130, y=470)

l27 = Label(frame1, text="Price:60", font="aeriel 10 bold")
l27.place(x=140, y=490)

my_spin9 = Spinbox(frame1, from_=0, to=10, width=4)
my_spin9.place(x=150, y=510)

# image 10 or lassi
img10 = PhotoImage(file="C:\\Users\\Acer\\Desktop\\first_sem\\first_sem\\lassi1.png")
l28 = Label(frame1, image=img10)
l28.place(x=230, y=450)

l29 = Label(frame1, text="Lassi", font="aeriel 10 bold")
l29.place(x=350, y=470)

l30 = Label(frame1, text="Price:100", font="aeriel 10 bold")
l30.place(x=340, y=490)

my_spin10 = Spinbox(frame1, from_=0, to=10, width=4)
my_spin10.place(x=350, y=510)

# image 11 or bubble tea
img11 = PhotoImage(
    file="C:\\Users\\Acer\\Desktop\\first_sem\\first_sem\\bubble tea1.png"
)
l28 = Label(frame1, image=img11)
l28.place(x=460, y=430)

l29 = Label(frame1, text="Bubble tea", font="aeriel 10 bold")
l29.place(x=530, y=470)

l30 = Label(frame1, text="Price:180", font="aeriel 10 bold")
l30.place(x=535, y=490)

my_spin11 = Spinbox(frame1, from_=0, to=10, width=4)
my_spin11.place(x=545, y=510)


win.mainloop()
