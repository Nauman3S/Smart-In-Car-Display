import tkinter
from tkinter import *
from PIL import Image, ImageTk
import random
import datetime
from commHandler import *
from MPU6050Handler import *
from DHT22Handler import *
from touchHandler import *
from brightnessController import *

brightnessCounter=0
# start from 60 and clockwise
seconds_coords = [[220, 10], []]
root = Tk()
activeFrame = 0

container1 = tkinter.Frame(root, width=480, height=480)
container1.place(x=0, y=0)
container2 = tkinter.Frame(root, width=480, height=480)
container2.place(x=0, y=0)
container2.place_forget()


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
image1 = Image.open("artwork/1.png")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(container1, image=test)
label1.image = test
label1.place(x=0, y=0)


image2 = Image.open("artwork/2.png")
test2 = ImageTk.PhotoImage(image2)
labeli2 = tkinter.Label(container2, image=test2)
labeli2.image = test2
labeli2.place(x=0, y=0)


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
    if(brightnessCounter>=12):
        setBrightness(100)
    brightnessCounter=0#reset brightness
    if(activeFrame == 0):
        activeFrame = 1
        container2.place(x=0, y=0)
        container1.place_forget()
        container2.tkraise()
    elif(activeFrame == 1):
        activeFrame = 0
        container1.place(x=0, y=0)
        container2.place_forget()
        container1.tkraise()


def updateData():
    global humid_var, inside_temp_var, outside_temp_var, time_hr_var, time_mn_var, time_sc_var
    global brightnessCounter
    now = datetime.datetime.now()
    humid_var.set(str(getTHArray()[1]))
    inside_temp_var.set(str(getTHArray()[0]))
    outside_temp_var.set(str(getTHArray()[2]))
    brightnessCounter=brightnessCounter+1
    if(brightnessCounter>=12):
        setBrightness(15)
    # if(len(str(now.hour)) == 1):

    #     time_hr_var.set("0"+str(now.hour))
    # else:
    #     time_hr_var.set(str(now.hour))

    # if(len(str(now.minute)) == 1):
    #     time_mn_var.set("0"+str(now.minute))
    # else:
    #     time_mn_var.set(str(now.minute))

    # if(len(str(now.second)) == 1):
    #     time_sc_var.set("0"+str(now.second))
    # else:
    #     time_sc_var.set(str(now.second))

    root.after(1000, updateData)


def updateGForceData():
    global x1_var, x2_var, y1_var, y2_var

    loopGyro()
    loopTempHumidSensors()

    y1_var.set(str(getGyroData()[0]))
    y2_var.set(str(getGyroData()[1]))
    x1_var.set(str(getGyroData()[2]))
    x2_var.set(str(getGyroData()[3]))

    root.after(500, updateGForceData)


def serialListner():
    global ser, dataPacket
    if (ser.in_waiting > 0):
        line = ser.readline()
        lineDec = line.decode('utf-8').rstrip()
        print('data received: ', lineDec)
        print('crc calculated', crc8(line))
        if(integrtiyCheck(lineDec)):
            dataPacket = lineDec
        else:
            dataPacket = ""
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
    "Arial", 20), fg='white', bg='black')
humid_label.place(x=220, y=85)

inside_temp = tkinter.Label(container1, textvariable=inside_temp_var, font=(
    "Arial", 20), fg='white', bg='black')
inside_temp.place(x=350, y=300)

outside_temp = tkinter.Label(container1, textvariable=outside_temp_var, font=(
    "Arial", 20), fg='white', bg='black')
outside_temp.place(x=95, y=300)


time_hr = tkinter.Label(container1, textvariable=time_hr_var,
                        font=("Helvetica", 70), fg='white', bg='black')
time_hr.place(x=180, y=150)
time_mn = tkinter.Label(container1, textvariable=time_mn_var,
                        font=("Helvetica", 70), fg='white', bg='black')
time_mn.place(x=180, y=250)


time_sc = tkinter.Label(container1, textvariable=time_sc_var,
                        font=("Helvetica", 45), fg='white', bg='black')
time_sc.place(x=200, y=350)


# gforce layout

y1 = tkinter.Label(container2, textvariable=y1_var, font=(
    "Arial", 16), fg='green', bg='black')
y1.place(x=230, y=80)
y1 = tkinter.Label(container2, textvariable=y2_var, font=(
    "Arial", 16), fg='white', bg='black')
y1.place(x=230, y=350)

x2 = tkinter.Label(container2, textvariable=x2_var, font=(
    "Arial", 16), fg='red', bg='black')
x2.place(x=360, y=230)

x1 = tkinter.Label(container2, textvariable=x1_var, font=(
    "Arial", 16), fg='purple', bg='black')
x1.place(x=85, y=230)


root.after(1000, updateData)
root.after(500, updateGForceData)
root.after(300, dataProcess)
root.after(100, serialListner)
root.bind("<Button-1>", touchFunc)

root.mainloop()
