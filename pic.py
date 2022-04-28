from picamera import PiCamera
import time
import datetime
camera = PiCamera()

camera.capture('SHOOPS_Output.jpg')  