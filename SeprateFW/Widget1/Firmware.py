import os
# os.environ["SDL_VIDEO_CENTERED"] = "1"
import tkinter
from tkinter import *
# import pyglet
from PIL import Image, ImageTk
import random
import datetime
from commHandler import *
from DHT22Handler import *
from touchHandler import *
from brightnessController import *

# pyglet.font.add_file('artwork/3ds-maisfont/3ds.ttf')


brightnessCounter = 0
# start from 60 and clockwise
seconds_coords = [[220, 10], []]
root = Tk()
root.eval('tk::PlaceWindow . center')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
activeFrame = 0

container1 = tkinter.Frame(root, width=480, height=480)
container1.place(x=0, y=0)


humid_var = tkinter.StringVar()
inside_temp_var = tkinter.StringVar()
outside_temp_var = tkinter.StringVar()
time_hr_var = tkinter.StringVar()
time_mn_var = tkinter.StringVar()
time_sc_var = tkinter.StringVar()
time_date_var = tkinter.StringVar()
time_day_var = tkinter.StringVar()
inside_temp_var.set("0")
outside_temp_var.set("0")
humid_var.set("0")
time_hr_var.set("00")
time_mn_var.set("00")
time_sc_var.set("60")
time_date_var.set("60")
time_day_var.set("60")




root.geometry("480x480+0+0")

# Create a photoimage object of the image in the path
image1 = Image.open("artwork/1.png")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(container1, image=test)
label1.image = test
label1.place(x=0, y=0)





def timeSet(hr, mn, sc, dt, dy):
    global time_hr_var, time_mn_var, time_sc_var, time_date_var, time_day_var
    time_hr_var.set(hr)
    time_mn_var.set(mn)
    time_sc_var.set(sc)
    time_day_var.set(dy)
    time_date_var.set(dt)


def touchFunc(n):
    global activeFrame, brightnessCounter
    print('screen touched')
   

def updateData():
    global humid_var, inside_temp_var, outside_temp_var, time_hr_var, time_mn_var, time_sc_var
    global brightnessCounter
    now = datetime.datetime.now()
    humid_var.set(str(getTHArray()[1]))
    inside_temp_var.set(str(getTHArray()[0]))
    outside_temp_var.set(str(getTHArray()[2]))
    brightnessCounter = brightnessCounter+1
    if(brightnessCounter >= 12):
        setBrightness(15)

    root.after(1000, updateData)



def serialListner():
    global ser, dataPacket
    serER = 0
    try:
        if (ser.in_waiting > 0):
            line = ser.readline()
            lineDec = line.decode('utf-8').rstrip()
            print('data received: ', lineDec)
            print('crc calculated', crc8(line))
            if(integrtiyCheck(lineDec)):
                dataPacket = lineDec
            else:
                dataPacket = ""
    except Exception as e:
        serER = 1
    root.after(100, serialListner)


def dataProcess():

    dataV = getData()

    if(dataV != ""):
        dataArray = dataV.split(',')
        if(dataArray[0] == '1'):
            # clock data
            dimmingHandler(dataArray[1])
            timeSet(dataArray[3], dataArray[4], dataArray[5],
                    dataArray[1], dataArray[2])  # hr,mn,sc,date,day

    root.after(300, dataProcess)


humid_label = tkinter.Label(container1, textvariable=humid_var, font=(
    "Arial", 30), fg='white', bg='#071025')
humid_label.place(x=240, y=75)

inside_temp = tkinter.Label(container1, textvariable=inside_temp_var, font=(
    "Arial", 30), fg='white', bg='#071025')
inside_temp.place(x=380, y=220)

outside_temp = tkinter.Label(container1, textvariable=outside_temp_var, font=(
    "Arial", 30), fg='white', bg='#071025')
outside_temp.place(x=80, y=220)


time_hr = tkinter.Label(container1, textvariable=time_hr_var,
                        font=("Helvetica", 70), fg='white', bg='#071025')
time_hr.place(x=180, y=120)
time_mn = tkinter.Label(container1, textvariable=time_mn_var,
                        font=("Helvetica", 70), fg='white', bg='#071025')
time_mn.place(x=180, y=210)


time_sc = tkinter.Label(container1, textvariable=time_sc_var,
                        font=("Helvetica", 45), fg='white', bg='#071025')
time_sc.place(x=200, y=310)



root.after(1000, updateData)

root.after(300, dataProcess)
root.after(100, serialListner)
root.bind("<Button-1>", touchFunc)

root.mainloop()
