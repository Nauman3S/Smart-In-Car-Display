import tkinter
from tkinter import *
# import pyglet
from PIL import Image, ImageTk
import random
import datetime
from commHandler import *
from touchHandler import *
from brightnessController import *

# pyglet.font.add_file('artwork/3ds-maisfont/3ds.ttf')


brightnessCounter = 0
# start from 60 and clockwise
seconds_coords = [[220, 10], []]
root = Tk()
activeFrame = 0


container3 = tkinter.Frame(root, width=480, height=480)
container3.place(x=0, y=0)



batt_temp1 = tkinter.StringVar()
batt_temp2 = tkinter.StringVar()
batt_temp3 = tkinter.StringVar()
batt_volts = tkinter.StringVar()
batt_temp1.set('0')
batt_temp2.set('0')
batt_temp3.set('0')
batt_volts.set('0')

root.geometry("480x480+0+0")


image3 = Image.open("artwork/Widgets/Battery/BatteryWithoutData.png")
test3 = ImageTk.PhotoImage(image3)
labeli3 = tkinter.Label(container3, image=test3)
labeli3.image = test3
labeli3.place(x=0, y=0)




def touchFunc(n):
    global activeFrame, brightnessCounter
    print('screen touched')
  


def updateData():
    global humid_var, inside_temp_var, outside_temp_var, time_hr_var, time_mn_var, time_sc_var
    global brightnessCounter
    now = datetime.datetime.now()
    # humid_var.set(str(getTHArray()[1]))
    # inside_temp_var.set(str(getTHArray()[0]))
    # outside_temp_var.set(str(getTHArray()[2]))
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
            # timeSet(dataArray[3], dataArray[4], dataArray[5],
                    # dataArray[1], dataArray[2])  # hr,mn,sc,date,day

    root.after(300, dataProcess)



# battery layout

batt_t1 = tkinter.Label(container3, textvariable=batt_temp1, font=(
    "Arial", 40), fg='white', bg='#071025')
batt_t1.place(x=220, y=70)

batt_t2 = tkinter.Label(container3, textvariable=batt_temp2, font=(
    "Arial", 40), fg='white', bg='#071025')
batt_t2.place(x=370, y=160)

batt_t3 = tkinter.Label(container3, textvariable=batt_temp2, font=(
    "Arial", 40), fg='white', bg='#071025')
batt_t3.place(x=220, y=340)

batt_vol = tkinter.Label(container3, textvariable=batt_volts, font=(
    "Arial", 40), fg='white', bg='#071025')
batt_vol.place(x=70, y=170)




root.after(1000, updateData)
root.after(300, dataProcess)
root.after(100, serialListner)
root.bind("<Button-1>", touchFunc)

root.mainloop()
