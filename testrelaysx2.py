import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while (True):
    GPIO.output(17, 1)
    sleep(1)
    GPIO.output(17, 0)
    sleep(1)

