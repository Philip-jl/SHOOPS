import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

while (True):
    GPIO.output(22, 0)
    GPIO.output(27, 0)
    GPIO.output(17, 0)
    GPIO.output(18, 0)
    break
