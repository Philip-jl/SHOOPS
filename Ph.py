from contextlib import redirect_stderr
from ctypes.wintypes import PSHORT
import cv2 as cv
import numpy as np
import argparse as arg
from MainSS import Ph_RGB 
from MainSS import Ph_HSV

PH = Ph_HSV[0]
PS = Ph_HSV[1]
PV = Ph_HSV[2]
Pr = Ph_RGB[0]
Pg = Ph_RGB[1]
Pb = Ph_RGB[2]

#red (2)
if PH > 350 and PH < 360: 
	#number of if and elif will be deternimed by how many tabs are in the color area
	if PH > 350 and PH < 355:
		Ph_value=6.0
	elif PH > 355 and PH < 360:
		Ph_value=6.5
	else:
		#value will be in the general range of where it is at
		Ph_value= 6.5
elif PH > 0  and PH < 30: 
	#number of if and elif will be deternimed by how many tabs are in the color area
	if PH > 0 and PH < 10:
		Ph_value=6.6
	elif PH > 10 and PH < 20:
		Ph_value=7.0
	elif PH > 20 and PH < 30:
		Ph_value=7.5
	else:
		#value will be in the general range of where it is at
		Ph_value= 7.0
elif PH > 30  and PH < 70: 
	#number of if and elif will be deternimed by how many tabs are in the color area
	if PH > 40 and PH < 50:
		Ph_value=8
	elif PH > 50 and PH < 60:
		Ph_value=8.5
	elif PH > 60 and PH < 70:
		Ph_value=9
	else:
		#value will be in the general range of where it is at
		Ph_value= 8.5
else:
	Ph_value = [1000 ,'error. please manually inspect image for any opjects obstructing camera view or skewing color detection']
print("PH value is", Ph_value)
cv.waitKey(0)