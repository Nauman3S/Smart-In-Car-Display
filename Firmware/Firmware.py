import tkinter
from tkinter import *
from PIL import Image, ImageTk
import random
import datetime

#start from 60 and clockwise
seconds_coords=[[220,10],[]]
root = Tk()


humid_var = tkinter.StringVar()
inside_temp_var = tkinter.StringVar()
outside_temp_var = tkinter.StringVar()
time_hr_var = tkinter.StringVar()
time_mn_var = tkinter.StringVar()
time_sc_var = tkinter.StringVar()
inside_temp_var.set("0")
outside_temp_var.set("0")
humid_var.set("0")
time_hr_var.set("00")
time_mn_var.set("00")
time_sc_var.set("60")

root.geometry("480x480+0+0")

# Create a photoimage object of the image in the path
image1 = Image.open("artwork/1.png")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(root,image=test)
label1.image = test
label1.place(x=0, y=0)

def touchFunc(n):
    print('screen touched')
def updateData():
    global humid_var, inside_temp_var, outside_temp_var, time_hr_var, time_mn_var, time_sc_var
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
    
    if(len(str(now.second)) == 1):
        time_sc_var.set("0"+str(now.second))
    else:
        time_sc_var.set(str(now.second))

    root.after(1000, updateData)


humid_label = tkinter.Label(root, textvariable=humid_var, font=(
    "Arial", 20), fg='white', bg='black')
humid_label.place(x=220, y=85)

inside_temp = tkinter.Label(root, textvariable=inside_temp_var, font=(
    "Arial", 20), fg='white', bg='black')
inside_temp.place(x=350, y=300)

outside_temp = tkinter.Label(root, textvariable=outside_temp_var, font=(
    "Arial", 20), fg='white', bg='black')
outside_temp.place(x=95, y=300)


time_hr = tkinter.Label(root, textvariable=time_hr_var,
                        font=("Helvetica", 70), fg='white', bg='black')
time_hr.place(x=180, y=150)
time_mn = tkinter.Label(root, textvariable=time_mn_var,
                        font=("Helvetica", 70), fg='white', bg='black')
time_mn.place(x=180, y=250)



time_sc = tkinter.Label(root, textvariable=time_sc_var,
                        font=("Helvetica", 45), fg='white', bg='black')
time_sc.place(x=200, y=350)


root.after(1000, updateData)
root.bind("<Button-1>", touchFunc)

root.mainloop()
