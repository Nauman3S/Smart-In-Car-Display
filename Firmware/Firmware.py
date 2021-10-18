import tkinter
from tkinter import *
from PIL import Image, ImageTk
import random
import datetime


root = Tk()

humid_var = tkinter.StringVar()
inside_temp_var = tkinter.StringVar()
outside_temp_var = tkinter.StringVar()
time_hr_var = tkinter.StringVar()
time_mn_var = tkinter.StringVar()
inside_temp_var.set("0")
outside_temp_var.set("0")
humid_var.set("0")
time_hr_var.set("00")
time_mn_var.set("00")

root.geometry("480x480+0+0")

# Create a photoimage object of the image in the path
image1 = Image.open("artwork/1.png")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)


def updateData():
    global humid_var, inside_temp_var, outside_temp_var, time_hr_var, time_mn_var
    now = datetime.datetime.now()
    humid_var.set(str(random.randint(10, 80)))
    inside_temp_var.set(str(random.randint(10, 80)))
    outside_temp_var.set(str(random.randint(10, 80)))
    if(len(str(now.hour)) == 1):

        time_hr_var.set("0"+str(now.hour))
    else:
        time_hr_var.set(str(now.hour))

    if(len(str(now.minute)) == 1):
        time_mn_var.set("0"+str(now.minute))
    else:
        time_mn_var.set(str(now.minute))

    root.after(1000, updateData)


humid_label = tkinter.Label(root, textvariable=humid_var, font=(
    "Arial", 25), fg='white', bg='black')
humid_label.place(x=220, y=60)

inside_temp = tkinter.Label(root, textvariable=inside_temp_var, font=(
    "Arial", 25), fg='white', bg='black')
inside_temp.place(x=360, y=150)

outside_temp = tkinter.Label(root, textvariable=outside_temp_var, font=(
    "Arial", 25), fg='white', bg='black')
outside_temp.place(x=85, y=150)


time_hr = tkinter.Label(root, textvariable=time_hr_var,
                        font=("Helvetica", 80), fg='white', bg='black')
time_hr.place(x=170, y=140)
time_mn = tkinter.Label(root, textvariable=time_mn_var,
                        font=("Helvetica", 80), fg='white', bg='black')
time_mn.place(x=170, y=250)


root.after(1000, updateData)
root.mainloop()
