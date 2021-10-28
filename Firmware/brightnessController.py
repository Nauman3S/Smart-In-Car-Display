import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)
pwm = GPIO.PWM(19, 64)

def setBrightness(val):
    global pwm
    pwm.start(val) # brightness 0-100