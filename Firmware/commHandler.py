import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
s = [0]

dataPacket = ""


def getData():
    return dataPacket


def crc8(binarydata):

    crc = 0
    for i in range(len(binarydata)):
        byte = binarydata[i]
        for b in range(8):
            fb_bit = (crc ^ byte) & 0x01
            if fb_bit == 0x01:
                crc = crc ^ 0x18
            crc = (crc >> 1) & 0x7f
            if fb_bit == 0x01:
                crc = crc | 0x80
            byte = byte >> 1
    return crc


def integrtiyCheck(val):

    if(val[0] == "1" or val[0] == "2" or val[0] == "3"):
        return True
    else:
        return False


print(crc8(b'test'))

ser.flush()


def dimmingHandler(val):
    print('dim value ', val)
