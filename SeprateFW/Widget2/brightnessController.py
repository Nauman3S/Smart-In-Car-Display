try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(19, GPIO.OUT)
    pwm = GPIO.PWM(19, 64)
    gpioEr=0

except Exception as e:
    print('e',e)
    gpioEr=1


def setBrightness(val):
    global pwm, gpioEr
    if(gpioEr==0):
        try:
            pwm.start(val) # brightness 0-100
        except Exception as e:
            print('e',e)