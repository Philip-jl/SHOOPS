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
    #dirty valve open
    sleep(5)
    GPIO.output(18, 1)
    sleep(20) #in final version we will add s needed to hit 150s goal
    print('0s  dirty open - pump start')
    GPIO.output(22, 1)
    sleep(.5)
    GPIO.output(22, 0)
    sleep(.5)
    GPIO.output(22, 1)
    sleep(.5)
    GPIO.output(22, 0)
    sleep(.5)
    GPIO.output(22, 1)
    sleep(.5)
    GPIO.output(22, 0)
    sleep(.5)
    GPIO.output(22, 1)
    sleep(.5)
    GPIO.output(22, 0)
    print('s  dirty close')
    sleep(10)
    #clean valve open
    print('s clean open')
    GPIO.output(27, 1)
    sleep(4)
    print('s clean close')
    GPIO.output(27, 0)
    sleep(50)
    #release valve open
    print('s drain open')#drain might need to stop after the whole bag is empty
    GPIO.output(17, 1)
    sleep(5)
    print('s drain close - pump stop ')
    GPIO.output(17, 0)
    GPIO.output(17, 1)
    sleep(5)
    print('s drain close - pump stop ')
    GPIO.output(17, 0)
    GPIO.output(17, 1)
    sleep(5)
    print('s drain close - pump stop ')
    GPIO.output(17, 0)
    GPIO.output(18, 0)
    #bring this back for pic at the end im just testing time stuff rn
    sleep(10)
    print('75 sec')
    camera = PiCamera()
    camera.capture('SHOOPS_Output.jpg')
    break
GPIO.cleanup()   
#take picture
#    GPIO.output(18, 1)
#    sleep(1)
#    GPIO.output(18, 0)
#    sleep(1)
    