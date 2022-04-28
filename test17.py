import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
#  This code controls the relays of the SHOOPS with all the components plugged into
#  the NO(normally open) configuration. This means all components are off by default.
#  In addition to this, below are the list of wires going into the pi GPIO pins with
#  wire colors and parts being controlled! :D

#|Color      |  GPIO pin  |   Function
#---------------------------------------
#orange wire => 18       =>  pump power
#yellow wire => 22       =>  dirty to chamber solenoid
#green wire  => 27       =>  clean to chamber solenoid
#blue wire   => 17       =>  chambers to pump reflow solenoid

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

while (True):
    GPIO.output(17, 1)
    sleep(10)
    print('s drain close - pump stop ')
    GPIO.output(17, 0)
   # GPIO.output(18, 0)
    break
GPIO.cleanup() 