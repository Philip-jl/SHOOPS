from contextlib import redirect_stderr
from ctypes.wintypes import PSHORT
import cv2 as cv
import numpy as np
import argparse as arg
from MainSS_Dirty import c2_Ph_RGB 
from MainSS_Dirty import c2_Ph_HSV
from MainSS_Clean import c1_Ph_RGB 
from MainSS_Clean import c1_Ph_HSV

PHD = c2_Ph_HSV[0]
PHC = c1_Ph_HSV[0]



#red (2)
if PHC > 350 and PHC < 360: 
	#number of if and elif will be deternimed by how many tabs are in the color area
	if PHC > 350 and PHC < 355:
		c1_Ph_value=6.0
	elif PHC > 355 and PHC < 360:
		c1_Ph_value=6.5
	else:
		#value will be in the general range of where it is at
		c1_Ph_value= 6.5
elif PHC > 0  and PHC < 30: 
	#number of if and elif will be deternimed by how many tabs are in the color area
	if PHC > 0 and PHC < 10:
		c1_Ph_value=6.6
	elif PHC > 10 and PHC < 20:
		c1_Ph_value=7.0
	elif PHC > 20 and PHC < 30:
		c1_Ph_value=7.5
	else:
		#value will be in the general range of where it is at
		c1_Ph_value= 7.0
elif PHC > 30  and PHC < 70: 
	#number of if and elif will be deternimed by how many tabs are in the color area
	if PHC > 40 and PHC < 50:
		c1_Ph_value=8
	elif PHC > 50 and PHC < 60:
		c1_Ph_value=8.5
	elif PHC > 60 and PHC < 70:
		c1_Ph_value=9
	else:
		#value will be in the general range of where it is at
		c1_Ph_value= 8.5
else:
	c1_Ph_value = [1000 ,'error']



#red (2)
if PHD > 350 and PHD < 360: 
	#number of if and elif will be deternimed by how many tabs are in the color area
	if PHD > 350 and PHD < 355:
		c2_Ph_value=6.0
	elif PHD > 355 and PHD < 360:
		c2_Ph_value=6.5
	else:
		#value will be in the general range of where it is at
		c2_Ph_value= 6.5
elif PHD > 0  and PHD < 30: 
	#number of if and elif will be deternimed by how many tabs are in the color area
	if PHD > 0 and PHD < 10:
		c2_Ph_value=6.6
	elif PHD > 10 and PHD < 20:
		c2_Ph_value=7.0
	elif PHD > 20 and PHD < 30:
		c2_Ph_value=7.5
	else:
		#value will be in the general range of where it is at
		c2_Ph_value= 7.0
elif PHD > 30  and PHD < 70: 
	#number of if and elif will be deternimed by how many tabs are in the color area
	if PHD > 40 and PHD < 50:
		c2_Ph_value=8
	elif PHD > 50 and PHD < 60:
		c2_Ph_value=8.5
	elif PHD > 60 and PHD < 70:
		c2_Ph_value=9
	else:
		#value will be in the general range of where it is at
		c2_Ph_value= 8.5
else:
	c2_Ph_value = [1000 ,'error']

#print( c1_Ph_value)
#print( c2_Ph_value)
