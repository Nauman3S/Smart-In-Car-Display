import tkinter
from tkinter import *
# import pyglet
from PIL import Image, ImageTk
import random
import datetime
from commHandler import *
from MPU6050Handler import *
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


container2 = tkinter.Frame(root, width=480, height=480)
container2.place(x=0, y=0)







y1_var = tkinter.StringVar()
y2_var = tkinter.StringVar()
x1_var = tkinter.StringVar()
x2_var = tkinter.StringVar()

x2_var.set(".")
x1_var.set(".")
y1_var.set(".")
y2_var.set(".")


batt_temp1 = tkinter.StringVar()
batt_temp2 = tkinter.StringVar()
batt_temp3 = tkinter.StringVar()
batt_volts = tkinter.StringVar()
batt_temp1.set('0')
batt_temp2.set('0')
batt_temp3.set('0')
batt_volts.set('0')

root.geometry("480x480+0+0")



image2 = Image.open("artwork/2.png")
test2 = ImageTk.PhotoImage(image2)
labeli2 = tkinter.Label(container2, image=test2)
labeli2.image = test2
labeli2.place(x=0, y=0)





def touchFunc(n):
    global activeFrame, brightnessCounter
    print('screen touched')
  




def updateGForceData():
    global x1_var, x2_var, y1_var, y2_var,gforceData

    loopGyro()
    # loopTempHumidSensors()
    y1.place(x=gforceData[0], y=gforceData[1])
    
    # y1_var.set(str(getGyroData()[0]))
    # y2_var.set(str(getGyroData()[1]))
    # x1_var.set(str(getGyroData()[2]))
    # x2_var.set(str(getGyroData()[3]))

    root.after(500, updateGForceData)


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
            #         dataArray[1], dataArray[2])  # hr,mn,sc,date,day

    root.after(300, dataProcess)




# gforce layout

y1 = tkinter.Label(container2, textvariable=y1_var, font=(
    "Arial", 8, 'bold'), fg='yellow', bg='yellow', height=1, width=1)
y1.place(x=230, y=80)



root.after(500, updateGForceData)
root.after(300, dataProcess)
root.after(100, serialListner)
root.bind("<Button-1>", touchFunc)

root.mainloop()
