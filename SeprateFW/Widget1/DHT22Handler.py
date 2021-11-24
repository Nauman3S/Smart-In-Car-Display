dhtAvailable=0
try:
    import Adafruit_DHT

    DHT_SENSOR1 = Adafruit_DHT.DHT22
    DHT_PIN1 = 16

    DHT_SENSOR2 = Adafruit_DHT.DHT22
    DHT_PIN2 = 18
    dhtAvailable=1
except Exception as e:
    print("E:",e)
    dhtAvailable=0

thArray = [0, 0, 0, 0]


def loopTempHumidSensors():
    global thArray
    try:
        humidity1, temperature1 = Adafruit_DHT.read_retry(DHT_SENSOR1, DHT_PIN1)
        humidity2, temperature2 = Adafruit_DHT.read_retry(DHT_SENSOR2, DHT_PIN2)
        if humidity1 is not None and temperature1 is not None:
            thArray[0] = temperature1
            thArray[1] = humidity1
        else:
            thArray[0] = 0
            thArray[1] = 0

        if humidity2 is not None and temperature2 is not None:
            thArray[2] = temperature1
            thArray[3] = humidity1
        else:
            thArray[2] = 0
            thArray[3] = 0

    except Exception as e:
        #print("E:",e)
        dhtAvailable=0

def getTHArray():
    global thArray
    return thArray
