import tkinter
from tkinter import *
from PIL import Image, ImageTk
import random
import datetime


root = Tk()

y1_var = tkinter.StringVar()
y2_var = tkinter.StringVar()
x1_var = tkinter.StringVar()
x2_var = tkinter.StringVar()

x2_var.set("0")
x1_var.set("0")
y1_var.set("0")
y2_var.set("0")

root.geometry("480x480+0+0")

# Create a photoimage object of the image in the path
image1 = Image.open("artwork/2.png")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)


def updateData():
    global x1_var,x2_var,y1_var,y2_var
    
    y1_var.set(str(random.randint(10, 80)))
    y2_var.set(str(random.randint(10, 80)))
    x1_var.set(str(random.randint(10, 80)))
    x2_var.set(str(random.randint(10, 80)))

    root.after(1000, updateData)


y1 = tkinter.Label(root, textvariable=y1_var, font=(
    "Arial", 16), fg='green', bg='black')
y1.place(x=230, y=80)
y1 = tkinter.Label(root, textvariable=y2_var, font=(
    "Arial", 16), fg='white', bg='black')
y1.place(x=230, y=350)

x2 = tkinter.Label(root, textvariable=x2_var, font=(
    "Arial", 16), fg='red', bg='black')
x2.place(x=360, y=230)

x1 = tkinter.Label(root, textvariable=x1_var, font=(
    "Arial", 16), fg='purple', bg='black')
x1.place(x=85, y=230)





root.after(1000, updateData)


root.mainloop()
