import cv2 as cv
import numpy as np
import argparse as arg
from MainSS import Merc_RGB
from MainSS import Merc_HSV

MH = Merc_HSV[0]
MS = Merc_HSV[1]
MV = Merc_HSV[2]
Mr = Merc_RGB[0]
Mg = Merc_RGB[1]
Mb = Merc_RGB[2]

#color area 1
if MH >= 315 and MH <= 325:
	if MH >= 315 and MH <= 325:
		Merc_value= 0
	else:
		Merc_value= 0
#color area 2 
elif MH >= 213 and MH <= 217:
	if MH >= 213 and MH <= 217:
		Merc_value= 0.002
	else:
		Merc_value= 0.002
elif MH >= 277 and MH <= 293:
	if Mg >= 160 and Mg <= 170:
 		Merc_value = 0.005
	elif Mg >= 140 and Mg <= 150:
		Merc_value = 0.01
	elif Mg >= 90 and Mg <= 110:
		Merc_value = 0.02
	else:
		Merc_value=0.02
elif MH >= 250 and MH <= 260:
	if Mr <= 90 and Mr >= 103:
		Merc_value = 0.04
	elif Mr <= 48 and Mr >= 60:
		Merc_value = 0.08
	else:
		Merc_value=0.08
else:
	Merc_value = [1000 ,'error. please manually inspect image for any opjects obstructing camera view or skewing color detection']
print("Mercury value is", Merc_value)